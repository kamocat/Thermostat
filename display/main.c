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
#include <string.h> // for strcpy
#include "gfx.h"

int main(void) {
	gCoord		width, y, height;
	gFont		font1, font2, font3;
	gCoord		fheight1, fheight2;
	char		current_time[10];
	char		target_temp[5];
	char		current_temp[5];
	char		outside_temp[5];
	time_t 		t;

    // Initialize and clear the display
    gfxInit();

    // Get the screen size
    //width = gdispGetWidth();
	width = 320;
	height = 240;

    // Get the fonts we want to use
	font1 = gdispOpenFont("DejaVu*32");
	font2 = gdispOpenFont("DejaVu*12");
	font3 = gdispOpenFont("Large*");
	//font2 = gdispOpenFont("UI2*");
	//font2 = gdispOpenFont("Geosans*");
	//font2 = gdispOpenFont("Free*");
	//font2 = gdispOpenFont("Hellovetica*");
	//font2 = gdispOpenFont("babyblue*");
	//font2 = gdispOpenFont("PF Ronda*");
	//font2 = gdispOpenFont("Apple*");

	y = 0;
	fheight1 = gdispGetFontMetric(font1, gFontHeight)+2;
	fheight2 = gdispGetFontMetric(font2, gFontHeight)+2;

	// Update the time
	t = time(NULL);
	strftime(current_time, sizeof(current_time), "%R %p", localtime(&t));
	
	strcpy(current_temp, "68");
	strcpy(target_temp, "70");
	strcpy(outside_temp, "45");

	gdispFillStringBox(0, y, width/2,  fheight1, current_time, font1, GFX_BLACK, GFX_WHITE, gJustifyCenter);
	gdispFillStringBox(width/2, y, width/2,  fheight1, target_temp, font1, GFX_BLACK, GFX_WHITE, gJustifyCenter);
	y += fheight1+1;
	gdispFillStringBox(0, y, width/2,  fheight2, "Inside", font2, GFX_BLACK, GFX_WHITE, gJustifyCenter);
	gdispFillStringBox(width/2, y, width/2,  height-y, outside_temp, font1, GFX_BLACK, GFX_WHITE, gJustifyCenter);
y += fheight2;
	gdispFillStringBox(0, y, width/2,  fheight1, current_temp, font1, GFX_BLACK, GFX_WHITE, gJustifyCenter);

	
	// Wait forever
    while(1) {
    	gfxSleepMilliseconds(500);
    }   
}

