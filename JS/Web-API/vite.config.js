import { defineConfig } from 'vite'
import * as path from 'path';
import vue from '@vitejs/plugin-vue'


// https://vitejs.dev/config/
export default () => {
  const projectRootDir = path.resolve(__dirname);
  const root = process.cwd();

  return {
    root,
    plugins: [vue()],
    resolve: {
      alias: [
        // /@/xxxx => src/xxxx
        {
          find: /\/@\//,
          replacement: path.resolve(projectRootDir, 'src') + '/',
        },
      ]
    }
  }
}
