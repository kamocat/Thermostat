#include <stdio.h>
#include <stdlib.h>
#include "js0n/src/js0n.h"

#define NUM_TOKENS 10

int main( int argc, char ** argv ){
	char * json_string;
  size_t r;
//	const char * url = "https://api.weather.gov/stations/CRVO/observations/latest";
  FILE * input;

  json_string = malloc(5000);
  
  if( argc > 1 ){
    input = fopen(argv[1], "r");
  } else {
    input = fopen("sample.json", "r");
  }
  
  r = fread( json_string, 1, 5000, input );
  size_t rb;
  char * properties = js0n("properties", 0, json_string, r, &rb);
  size_t len;
  char * description = js0n("textDescription", 0, properties, rb, &len);
  printf("Description: %.*s\r\n", len, description);
  char * temperature = js0n("temperature", 0, properties, rb, &len);
  temperature = js0n("value", 0, temperature, len, &len);
  printf("Temperature: %.*s Celcius\r\n", len, temperature);

  

  fclose( input );
  free( json_string);
	return 0;
}
