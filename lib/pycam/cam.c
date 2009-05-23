#include <webcam.h>
#include <stdio.h>
#include <stdlib.h>

int camMAX_DEVICES = 32;
int camInitialized = 0;
CDevice camDevices[32];
CPixelFormat camPixelFormats[32];
CFrameSize camFrameSizes[128];
CFrameInterval camFrameIntervals[128];
unsigned int camNumDevices = 0;

void check(CResult result) {
  if (result != C_SUCCESS) {
    fprintf(stderr, "c_init failed with %i\n", result);
    if (camInitialized) { c_cleanup(); }
    exit(1);
  }
}

CDevice* camEnumDevices() {
  CDevice* devices;
  unsigned int size = sizeof(CDevice)*camMAX_DEVICES, count = camMAX_DEVICES;
  check(c_enum_devices(camDevices,&size,&count));
  camNumDevices = count;
  return camDevices;
}

int main(int argc, char* argv[]) {
  check(c_init());
  camInitialized = 1;
  camEnumDevices();
  
  if (numDevices == 0) {
    fprintf(stderr, "no cameras found\n");
    exit(1);
  }

  CHandle handle = c_open_device(camDevices[0].name);
  

  c_cleanup();
}
