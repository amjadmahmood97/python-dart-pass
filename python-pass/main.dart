/*
Can't set const with time,because const A variable that is declared using the const keyword cannot be assigned any other value.
Also, the variable is known as a compile-time constant, which in turn means that its value must be declared while compiling the program.

And This is the correct solution
void main() {
  var hour = DateTime.now();
  print(hour);
}
*/

