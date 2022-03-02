# Vue 3 + Vite + tauri

This template should help get you started developing with Vue 3 in Vite, and can build desktop application with **tauri**. It's fast!

The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.


## Vite.js
[Vite.js](https://vitejs.dev/) is a new modern bundler for javascript which is blazing fast and includes many sensible defaults.

## Tauri
[Tauri](https://github.com/tauri-apps/tauri) is a new modern technology to turn your web apps into a desktop app for multiple platforms (Windows, MacOS, Linux, android and ios soon). Tauri apps have very small file size and tiny memory consumption.

## Vue 3
[Vue.js](https://vuejs.org/) is an incremental frontend framework which is an absolute joy to work with. It has seen very impressive improvements in version 3 including Composition Api, script setup, dynamic css binding and ... .

### Bonus: Vue Global Api
[Vue Global Api](https://github.com/antfu/vue-global-api) globally registers commonly used composition api functions such as `ref`, `reactive` and ... . makes your `script setup` sections cleaner.

## Installation
- Ready your workspace according to tauri. [Tauri Getting Started](https://tauri.studio/en/docs/getting-started/intro/)

  - **Note:** You only need to install global things such as rust and other os level packages. Any thing related to application itself is already installed and ready for you.

- Clone repository `git clone https://github.com/yooneskh/vite-tauri-template app-name`

- `yarn` or `npm i`

- Modify these files according to your app.
  - `index.html`
  - `package.json`
  - `public/favicon.ico`
  - `src/assets/logo.*`
  - `src-tauri/tauri.conf.json`

## Usage

- `pnpm dev` launches vite and you can test and develop your app in the browser at `http://localhost:8080`.

- `pnpm dev` launches vite and configures ynetwork to use tauri for api calls. Use this if you want to test your app in tauri dev mode.

- `pnpm dev:tauri` launches tauri in dev mode and you can see your app in tauri window.

- `pnpm build` builds web application and packages them with tauri in `src-tauri/target`

- `pnpm build:web` only builds the web application and puts it in `./dist` directory. You should not normally want this. Difference of this web app with the one build with normal `yarn build` is that this one uses axios for network calls.

## License
Do whatever you want with it!