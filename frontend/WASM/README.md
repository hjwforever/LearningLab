## 安装 emscripten 环境

```
# 获取到工具包
git clone https://github.com/emscripten-core/emsdk.git

# 获取最新版本的emsdk（第一次克隆时不需要）
git  pull

# 下载最新的SDK工具,window中指令为emsdk,且需要下载python软件
./emsdk install latest

# 使当前用户的“最新” SDK处于“活动”状态。（写入.emscripten文件）
./emsdk activate latest

# 激活PATH和在当前终端中其他环境变量,window中为emsdk_env.bat而不是
source ./emsdk_env.sh

# 命令行中运行指令emcc -v
# 如无法运行则说明环境配置没有成功,需要手动配置
# 找到emsdk下的emsdk_env.bat文件编辑,最后一行写pause,然后看命令行的输出,根据命令行来对系统环境变量进行配置
```

## 确保有gcc编译环境
命令行输入`gcc`进行验证, 正常输出如下：
```bash
$ gcc
gcc: fatal error: no input files
compilation terminated.
```
## 编译指令及问题
### c++的编译
```bash
emcc test.c -s WASM=1 -o test.html
```
生成除了`Wasm`二进制文件和`JavaScript`包装文件外的可执行`HTML`文件，还可以指定一个以 `.html`结尾的输出文件；那么就会输出html以及js,如果是js后缀的输出文件,那么就不会再生成一个html
`xxx.wasm`必须和`xxx.js`在同一路径下
不能在浏览器里通过`file://`协议简单的打开`HTML`文件，因为在`file`协议里跨源请求时不被允许的，需要通过开启一个`http`服务来打开文件， 如`http-server`、`nginx`等。也通过`EmscriptSDK`的 `emrun`来提供一个`http服务`：

```bash
# htt-server 默认为http://localhost:8080
$ http-server .
# emrun，地址为:http://localhost:8000/xxx.html
$ emrun --no_browser --port 8000 ./
```
### c的编译
  `Emscripten`生成的代码只会调用`main()`函数，其他函数将被视为无用代码。
为了避免这件事发生，我们需要在C函数名之前，添加`EMSCRIPTEN_KEEPALIVE`，它在`emscripten.h`中声明。
#### C
```c
#include <stdio.h>
#include <emscripten/emscripten.h>

int main(int argc, char ** argv) {
    printf("Hello World\n");
}

#ifdef __cplusplus
extern "C" {
#endif

int EMSCRIPTEN_KEEPALIVE myFunction(int argc, char ** argv) {
  printf("我的函数已被调用\n");
}

#ifdef __cplusplus
}
#endif
```
#### 编译指令
```bash
emcc -o xxx.html xxx.c -s WASM=1 -s "EXPORTED_RUNTIME_METHODS=['ccall']"
```
### wasm及其js的引入
  `js`的引入以及函数的调用都需要以**异步**的形式调用, 不然会报错

## 参考
- https://www.yuque.com/docs/share/d3605332-eed1-4aad-a025-006b21d42bc4