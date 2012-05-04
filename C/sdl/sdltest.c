//sdltest.c

/* Includes */
#include </usr/include/SDL/SDL.h>

SDL_Surface *screen;
SDL_Event event;

/* Main */
int main()
{
	/* Initialize SDL */
	SDL_Init(SDL_INIT_VIDEO);
	/* Set video mode */
	screen = SDL_SetVideoMode(640,480,32,SDL_SWSURFACE);
	/* Enter a loop */
	while(1)
	{
		/* Check for user quit */
		while(SDL_PollEvent(&event))
		{
			if(event.type == SDL_QUIT)
			{
				/* Stop the test */
				SDL_Quit();
				return 0;
			}
		}
		/* Fill with black */
		SDL_FillRect(screen,&screen->clip_rect,SDL_MapRGB(screen->format,0,0,0));
		/* Update */
		SDL_Flip(screen);
	}
}

