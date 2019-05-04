#include <stdio.h>
#include <stdlib.h>
//#include "js0n/src/js0n.h"

int main( int argc, char ** argv ){
	char * json_string;
  size_t r;
  FILE * input;

  json_string = malloc(500);
  
  if( argc > 1 ){
    input = fopen(argv[1], "r");
  } else {
    input = fopen("input", "r");
  }
  
  while( 1 ){
    r = fread( json_string, 1, 500, input );
    if( r ){
      printf("%d characters: %.*s", r, r, json_string);
    }
  }
/*
  size_t len;
  char * current = js0n("current", 0, json_string, r, &len);
  printf("Current temp: %.*s\r\n", len, current);
  char * target = js0n("target", 0, json_string, r, &len);
  printf("Target temp: %.*s\r\n", len, target);
*/

  

  fclose( input );
  free( json_string);
	return 0;
}
