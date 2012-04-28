echo -n "Password1"

stty -echo
read password
stty echo

echo ""
echo you entered $password

