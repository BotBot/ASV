from opencv.cv import *
from opencv.highgui import *

def flatten(l):
  v = []
  for x in l:
    if isinstance(x,list):
      v += x
    else:
      v.append(x)
  return v

def interleave(*ll):
  for i in xrange(max(map(len,ll))):
    for j in xrange(len(ll)):
      if i < len(ll[j]):
        yield ll[j][i]
      else:
        yield None
  

class Camera:
  def __init__(self, i=CV_CAP_ANY):
    self.cam = cvCreateCameraCapture(i)

  def release(self):
    return cvReleaseCapture(self.cam)

  def frame(self):
    return cvQueryFrame(self.cam)

  def grab(self):
    return cvGrabFrame(self.cam)

  def retrieve(self):
    return cvRetrieveFrame(self.cam)


class Window:
  if not hasattr(None,'thread_started'):
    thread_started = False

  def __init__(self, title="OpenCV", flags=CV_WINDOW_AUTOSIZE):
    if not self.thread_started:
      cvStartWindowThread()

    cvNamedWindow(title,flags)
    self.handle = cvGetWindowHandle(title)

  def close(self):
    cvDestroyWindow(self.title)

  @classmethod
  def close_all(self):
    cvDestroyAllWindows()

  @property
  def title(self):
    return cvGetWindowName(self.handle)

  def show(self,img):
    cvShowImage(self.title, img)


def Size(w,h):
  s = CvSize()
  s.width = w
  s.height = h
  return s



def _mat_similar(self, channels=None):
  return cvCreateImage(Size(self.width,self.height),
                       self.depth,
                       channels or self.nChannels)

def _mat_channels(self, *ii):
  mats = [None]*4
  for x in ii: mats[x] = self.similar(1)
  cvSplit(self,*mats)
  return [mats[x] for x in ii]

def _mat_merge(self, *mats):
  mats = list(mats) + [None]*(4-len(mats)) + [self]
  cvMerge(*mats)
  return self

def _mat_fill(self, *ii):
  cvSet(self,cvScalar(*ii))

def _mat_set_channel(self,chan,value):
  mats = [None]*4
  mats[chan] = self.similar(1)
  cvSet(mats[chan],cvScalar(value))
  self.merge(*mats)
  return self

def _mat_cvt_color(self, code, chan):
  mat = self.similar(chan)
  cvCvtColor(self,mat,code)
  return mat

def _mat_rgb2hsv(self):
  return self.cvt_color(CV_RGB2HSV,3)

def _mat_hsv2rgb(self):
  return self.cvt_color(CV_HSV2RGB,3)

def _mat_rgb2hue(self):
  hsv = self.rgb2hsv()
  hsv.set_channel(1,255) # sat
  hsv.set_channel(2,255) # val
  return hsv.hsv2rgb()

CvMat.similar = _mat_similar
CvMat.channels = _mat_channels
CvMat.merge = _mat_merge
CvMat.fill = _mat_fill
CvMat.set_channel = _mat_set_channel
CvMat.cvt_color = _mat_cvt_color
CvMat.rgb2hsv = _mat_rgb2hsv
CvMat.hsv2rgb = _mat_hsv2rgb
CvMat.rgb2hue = _mat_rgb2hue


def loop():
  c = Camera()
  w = Window()
  while cvWaitKeyC(1) == -1:
    w.show(c.frame())
  w.close()
  c.release()

def hueloop():
  c = Camera()
  w = Window()
  while cvWaitKeyC(10) == -1:
    w.show(c.frame().rgb2hue())
  w.close()
  c.release()
