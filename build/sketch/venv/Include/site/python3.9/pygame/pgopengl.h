#line 1 "c:\\Users\\matth\\OneDrive - University of Prince Edward Island\\XAC Management and Storage\\_Freedom Wing Project\\Latency_Tester\\venv\\Include\\site\\python3.9\\pygame\\pgopengl.h"
#if !defined(PGOPENGL_H)
#define PGOPENGL_H

/** This header includes definitions of Opengl functions as pointer types for
 ** use with the SDL function SDL_GL_GetProcAddress.
 **/

#if defined(_WIN32)
#define GL_APIENTRY __stdcall
#else
#define GL_APIENTRY
#endif

typedef void(GL_APIENTRY *GL_glReadPixels_Func)(int, int, int, int,
                                                unsigned int, unsigned int,
                                                void *);

typedef void(GL_APIENTRY *GL_glViewport_Func)(int, int, unsigned int,
                                              unsigned int);
#endif
