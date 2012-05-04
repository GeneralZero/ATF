#ifndef _MINITALK_H_
#define _MINITALK_H_

#include <signal.h>
//#include <unistd.h>
#include "../lib/my.h"

typedef struct	s_env
{
  pid_t		cpid;
  short		sigflag;
}	t_env;

#endif
