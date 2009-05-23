#include <webcam.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
  CResult result;
  result = c_init();
  if (result != C_SUCCESS) {
    fprintf(stderr, "c_init failed with %i", result);
  }
    
  c_cleanup();
}
