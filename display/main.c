/*
 * Copyright (c) 2012, 2013, Joel Bodenmann aka Tectu <joel@unormal.org>
 * Copyright (c) 2012, 2013, Andrew Hannam aka inmarket
 *
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *    * Redistributions of source code must retain the above copyright
 *      notice, this list of conditions and the following disclaimer.
 *    * Redistributions in binary form must reproduce the above copyright
 *      notice, this list of conditions and the following disclaimer in the
 *      documentation and/or other materials provided with the distribution.
 *    * Neither the name of the <organization> nor the
 *      names of its contributors may be used to endorse or promote products
 *      derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <time.h>
#include <locale.h>
#include <string.h> // for strlcpy
#include "gfx.h"
#include "js0n/src/js0n.h"
#include <stdio.h> // for file IO
#define STR_SIZE 10

int main(void) {
  char * input_string;
  FILE * input;
	gCoord		width, y, height;
	gFont		font1, font2, font3;
	gCoord		fheight1, fheight2, fheight3;
	char		current_time[STR_SIZE];
	char		* target_temp;
	char		* current_temp;
	char		outside_temp[STR_SIZE];
	time_t 		t;

    // Initialize and clear the display
    gfxInit();

  // Open the FIFO
  input = fopen("input", "r");
  input_string = (char *)gfxAlloc( 100 );

    // Get the screen size
    //width = gdispGetWidth();
	width = 320;
	height = 240;

    // Get the fonts we want to use
    font1 = gdispOpenFont("DejaVu*32");
    font2 = gdispOpenFont("DejaVu*12");
    font3 = gdispOpenFont("DejaVu*100");

    y = 0;
    fheight1 = gdispGetFontMetric(font1, gFontHeight)+2;
    fheight2 = gdispGetFontMetric(font2, gFontHeight)+2;
    fheight3 = gdispGetFontMetric(font3, gFontHeight)+2;


    // Wait forever
    while(1) {
      y = 0;
      // Update the time
      t = time(NULL);
      strftime(current_time, sizeof(current_time), "%I:%M %p", localtime(&t));
      
      // Get our new values from the FIFO
      size_t r = fread( input_string, 1, 100, input);
      fseek( input, r, SEEK_CUR );  // Move the file position
      size_t len1;
      size_t len2;
      current_temp = js0n("current", 0, input_string, r, &len1);
      target_temp = js0n("target", 0, input_string, r, &len2);
      strcpy(outside_temp, "45");

      gdispFillStringBox(0, y, width/2,  fheight1, current_time, font1, GFX_BLACK, GFX_WHITE, gJustifyCenter);
      if( target_temp ){
        target_temp[len2] = 0;
        gdispFillStringBox(width/2, y, width/2,  fheight1, target_temp, font1, GFX_BLACK, GFX_WHITE, gJustifyCenter);
      }
      y += fheight1+1;
      gdispFillStringBox(0, y, width/2,  fheight2, "Inside", font2, GFX_BLACK, GFX_WHITE, gJustifyCenter);
      gdispFillStringBox(width/2, y, width/2,  height-y, outside_temp, font1, GFX_BLACK, GFX_WHITE, gJustifyCenter);
    y += fheight2;
      if( current_temp ){
        current_temp[len1] = 0;
        gdispFillStringBox(0, y, width/2,  fheight3, current_temp, font3, GFX_BLACK, GFX_WHITE, gJustifyCenter);
      }

    	gfxSleepMilliseconds(500);
    }   

	
}

