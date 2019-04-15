#include <time.h>
#include <stdio.h>
#include <locale.h>

int main( int argc, char ** argv ){
	char buff[20];
	time_t t = time(NULL);
	const char * url = "https://api.weather.gov/stations/CRVO/observations/latest";
	
	strftime(buff, sizeof(buff), "%R %p", localtime(&t));
	puts(buff);

	return 0;
}