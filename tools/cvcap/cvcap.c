#include "opencv/cv.h"
#include "opencv/highgui.h"
#include <stdio.h>

/*  Example code from the OpenCV site to open a window
 *  and stream video from a camera.
 */

int main(int argc, char* argv[]) {
  CvCapture* capture = cvCaptureFromCAM(CV_CAP_ANY);
  int i = 0;

  if (!capture) {
    fprintf(stderr, "Can't find camera");
    return -1;
  }

  cvSetCaptureProperty(capture,CV_CAP_PROP_FPS,30);

  //cvNamedWindow("camcam", CV_WINDOW_AUTOSIZE);

  for (;;) {
    IplImage* frame = cvQueryFrame(capture);

    if (!frame) {
      fprintf(stderr,"Can't get frame");
      break;
    }

    //cvShowImage("camcam",frame);
    printf(".");
    fflush(stdout);

    /*
    if ((cvWaitKey(10) & 0xff) == 27) {
      break;
      }*/
  }

  cvReleaseCapture(&capture);
  //cvDestroyWindow("camcam");
  return 0;
}
