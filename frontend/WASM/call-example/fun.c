#include <stdio.h>
#include <emscripten/emscripten.h>

int main(int argc, char ** argv) {
  printf("Hello World\n");
  return 0;
}

#ifdef __cplusplus
extern "C" {
#endif

// c的编译
// Emscripten生成的代码只会调用main()函数，其他函数将被视为无用代码。
// 为了避免这件事发生，我们需要在C函数名之前，添加EMSCRIPTEN_KEEPALIVE，它在emscripten.h中声明。
int EMSCRIPTEN_KEEPALIVE myFunction(int argc, char ** argv) {
  printf("我的函数已被调用\n");
  return 0;
}

#ifdef __cplusplus
}
#endif