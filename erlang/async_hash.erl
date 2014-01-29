%% Erlang Assignment
%% Brian Ridings
%% Kenneth Goff

%%   name of module; must match file name
-module(assignment4).
%%   gotcha: function to be spawned must be exported too ... not enough to export only first_thread
-compile(first_thread).

-export ([first_thread/0, loop/3]).

loop(Threads, Pid2, Lists) -> 
	%io:fwrite("second thread is running~n"),
	%io:fwrite("Hash Table: ~p~n", [Lists]),
	receive
		{_, [Option, String]} -> 
			%io:fwrite("~p, ~p, ~p ~n", [Sender, Option, String]),
			case Option of
			1 -> 
				case addIfAbsent(String, Threads, Lists) of
					{Test, true} -> io:fwrite("~nString sucessfully added to table~n"),
						Pid2 ! {self(), Test},
						loop(Threads, Pid2, Test);
					{Test, false} -> io:fwrite("~nString already in table~n"),
						Pid2 ! {self(), Test},
						loop(Threads, Pid2, Test)
				end;
			2 -> 
				case removeIfPresent(String, Threads, Lists) of
					{Test, true} -> io:fwrite("~nString sucessfully removed from table~n"),
						Pid2 ! {self(), Test},
						loop(Threads, Pid2, Test);
					{Test, false} -> io:fwrite("~nString was not in table~n"),
						Pid2 ! {self(), Test},
						loop(Threads, Pid2, Test)
				end;
			3 -> 
				case lookup(String, Threads, Lists) of
					true -> io:fwrite("~nString is in table~n"),
						Pid2 ! {self(), Lists},
						loop(Threads, Pid2, Lists);
					false -> io:fwrite("~nString is not in table~n"),
						Pid2 ! {self(), Lists},
						loop(Threads, Pid2, Lists)
				end;
			_Else -> loop(Threads, Pid2, Lists)
			end
	end.

first_thread_loop(SecondThread) ->
	io:fwrite("1) Add to table ~n2) Delete from table ~n3) Lookup string ~n4) Exit~n"),
	{ok, [ Dig ]} = io:fread("Enter option: ", "~d"),
	case Dig of
		4 -> exit(SecondThread, "Exiting Program~p");
		_Else -> {ok, [ String ]} = io:fread("String: ", "~s"),
				%io:fwrite("~p ~p", [Dig, String]),
				SecondThread ! {self(),[Dig, String]},
				receive
					{_, NewString} -> io:fwrite("~p~n", [NewString]),
						first_thread_loop(SecondThread)
				end
	end.

first_thread() ->
	io:fwrite("first_thread: ~p~n", [self()]),
	SecondThread = spawn(assignment4, loop, [10, self(), [[], [], [], [], [], [], [], [], [], [] ]]),
	io:fwrite("PID of second thread = ~p~n", [SecondThread]),
	first_thread_loop(SecondThread).

	%loop([SecondThread], 10, [[], [], [], [], [], [], [], [], [], [] ]).

removeIfPresent(Element, Length, Lists) ->
	Hash = erlang:phash(Element, Length),
	Table = lists:nth(Hash, Lists),
	Ret1 = lists:member(Element, Table),
	{First, Last} = lists:split(Hash - 1, Lists),
	case Ret1 of
		true -> Ret = First ++ [lists:delete(Element, Table)] ++ lists:nthtail(1, Last),
			{Ret, true};
		false -> {Lists, false}
	end.

	
lookup(Element, Number, Lists) ->
	Hash = erlang:phash(Element, Number),
	Table = lists:nth(Hash, Lists),
	lists:member(Element, Table).

addIfAbsent(Element, Length, Lists) ->
	Hash = erlang:phash(Element, Length),
	Table = lists:nth(Hash, Lists),
	{First, Last} = lists:split(Hash - 1, Lists),
	case lists:member(Element, Table) of
		false -> Ret = First ++ [[Element | Table]] ++ lists:nthtail(1, Last),
			{Ret, true};
		true ->  {Lists, false}
	end.
	