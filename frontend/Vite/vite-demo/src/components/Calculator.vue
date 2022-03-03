<template>
  <div :style="styleVars" class="calculator-container">
    <transition name="slide">
      <div class="calc-wrapper" v-if="show">
        <div class="calculator">
          <div class="calculator-logs" ref="historyLog" v-if="isHistoryLogs">
            <span v-for="(log, index) in logs" :key="index" @click="logToValue(log)">{{ log }}</span>
          </div>

          <input readonly type="text" class="calculator-input" v-model="expression" />

          <div class="calculator-row">
            <div class="calculator-col">
              <button class="calculator-btn gray action" @click="clear()">AC</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn gray action" @click="deleteLastChar">&lsaquo;</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn gray action" @click="touchHandler('%')">&#37;</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn accent action" @click="touchHandler('÷')">&divide;</button>
            </div>
          </div>
          <div class="calculator-row">
            <div class="calculator-col">
              <button class="calculator-btn" @click="touchHandler('7')">7</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn" @click="touchHandler('8')">8</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn" @click="touchHandler('9')">9</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn accent action" @click="touchHandler('×')">&times;</button>
            </div>
          </div>
          <div class="calculator-row">
            <div class="calculator-col">
              <button class="calculator-btn" @click="touchHandler('4')">4</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn" @click="touchHandler('5')">5</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn" @click="touchHandler('6')">6</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn accent action" @click="touchHandler('-')">-</button>
            </div>
          </div>
          <div class="calculator-row">
            <div class="calculator-col">
              <button class="calculator-btn" @click="touchHandler('1')">1</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn" @click="touchHandler('2')">2</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn" @click="touchHandler('3')">3</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn accent action" @click="touchHandler('+')">+</button>
            </div>
          </div>
          <div class="calculator-row">
            <div class="calculator-col wide">
              <button class="calculator-btn" @click="touchHandler('0')">0</button>
            </div>
            <div class="calculator-col">
              <button class="calculator-btn action" @click="touchHandler('.')">.</button>
            </div>
            <div class="calculator-col">
              <button v-if="isResult" class="calculator-btn success action" @click="applyResult">ок</button>
              <button v-else class="calculator-btn accent action" @click="touchHandler('=')">=</button>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="opacity">
      <div v-if="show" @click="persistent ? '' : hideInterface()" class="backdrop"></div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, nextTick, onMounted, defineEmits } from 'vue'

const expression = ref('')
const isResult = ref(false)
const error = ref(false)
const show = ref(true)
const showStyles = ref(false)
const autoApply = ref(false)

const persistent = ref(false)
const historyLog = ref(null)
const logs = ref([])
const isHistoryLogs = ref(true)

const enableKeyboard = ref(true)

const zIndex = ref(1000)
const textColor = ref('#fff')
const bgColor = ref('#2f2f31')
const eventButtonsBgColor = ref('#424345')
const numberButtonsBgColor = ref('#616163')
const actionButtonsBgColor = ref('#f49e3f')
const actionSuccessButtonBgColor = ref('#3ff451')

const floatResultFixedCount = ref(3)

const styleVars = computed(() => ({
  '--calculator-container-text-color': textColor.value,
  '--calculator-container-bg-color': bgColor.value,
  '--calculator-container-event-btn-bg-color': eventButtonsBgColor.value,
  '--calculator-container-number-btn-bg-color': numberButtonsBgColor.value,
  '--calculator-container-action-btn-bg-color': actionButtonsBgColor.value,
  '--calculator-container-action-success-btn-bg-color': actionSuccessButtonBgColor.value,
  ...(showStyles.value && {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-end',
    alignItems: 'center',
    height: '100%',
    width: '100%',
    position: 'absolute',
    top: 0,
    left: 0,
    zIndex: zIndex.value
  })
}))

onMounted(() => {
  if (enableKeyboard.value) {
    document.addEventListener('keydown', keyboardHandler)
  }
})

const logToValue = (log) => {
  if (log) {
    expression.value = log.split('=')[1] // log.replace(/=.*/, '')
    isResult.value = false
  }
}

const deleteLastChar = () => {
  if (expression.value !== '0') {
    console.log('deleteLastChar ', expression.value)
    expression.value = expression.value.slice(0, -1)
    if (!expression.value) {
      expression.value = '0'
    }
  }
}

const keyboardHandler = (event) => {
  let allowValue = event.key.match(/[0-9%%÷×/*\-+=.,]|Backspace|Enter/)
  let input = allowValue ? allowValue.input : null
  if (input) {
    // adaptation of the key key to a common standard
    // replace the comma with a dot for universality with different layouts
    switch (input) {
      case ',':
        input = '.'
        break
      case '/':
        input = '÷'
        break
      case '*':
        input = '×'
        break
      case 'Enter':
        input = '='
        break
      case 'Backspace':
        return deleteLastChar()
    }
    prepareInput(input)
  }
}
const touchHandler = (value) => {
  prepareInput(value)
}
const prepareInput = (value) => {
  let inputIsAction = Number.isNaN(Number.parseInt(value))
  let lastSymbol = expression.value.slice(-1)
  let lastSymbolIsAction = Number.isNaN(Number.parseInt(lastSymbol))
  // console.log({value, expresion: expression.value, inputIsAction, lastSymbolIsAction, lastSymbol});
  // value set to zero - no action required
  if (expression.value === '0') {
    if (value === '0') {
      //
      return
    } else if (!inputIsAction) {
      return (expression.value = value)
    }
  }
  switch (true) {
    case inputIsAction && lastSymbolIsAction && value !== '.' && value !== '=':
      // replace the last character
      expression.value = expression.value.slice(0, -1) + value
      break
    case inputIsAction && value === '=':
      //  check for unfinished expressions - action pad at the end
      //  If available, remove symbols from the end and do the calculation
      if (lastSymbolIsAction) {
        expression.value = expression.value.slice(0, -1)
      }
      if (isResult.value) {
        applyResult()
      } else {
        calculate()
      }
      break
    case inputIsAction && value === '.':
      // Check if the expression is complete
      if (
        Array.isArray(expression.value.split(/[%÷×/*\-+]/)) &&
        (expression.value
          .split(/[%÷×/*\-+]/)
          .slice(-1)[0]
          .indexOf('.') > -1 ||
          lastSymbolIsAction)
      ) {
        break
      } else {
        isResult.value = false
        expression.value += value
      }
      break
    default:
      isResult.value = false
      expression.value += value
      // console.error('prepareInput', value);
      break
  }
}
const calculate = () => {
  error.value = false
  let log = expression.value
  // If the expression starts with a negative value "-"
  // then ignore the empty current value and just put the action sign
  let regex = /[%÷×/*\-+]/g
  let actions = expression.value.match(regex)

  if (!actions) {
    return (isResult.value = true)
  }
  let numbers = expression.value.split(regex)
  expression.value = numbers.reduce((str, currNum, index) => {
    if (currNum) {
      str = str + parseFloat(currNum) + (actions[index] || '')
    } else {
      str = str + (actions[index] || '')
    }
    return str
  }, '')

  // calculate results
  try {
    let result = eval(expression.value.replaceAll(/\÷/g, '/').replaceAll(/×/g, '*'))
    // console.warn({result},Number.isInteger(result));
    console.log(`result :`, result)
    expression.value = Number.isInteger(result)
      ? result.toString()
      : parseFloat(parseFloat(result).toFixed(floatResultFixedCount.value)).toString()
    isResult.value = true
    logs.value.push(log + `=${expression.value}`)
  } catch {
    // alert('Error eval: ' + expression.value);
    error.value = true
  }
  // scroll log to last action
  nextTick(() => {
    if (historyLog.value) {
      historyLog.value.scrollTop = historyLog.value.scrollHeight
    }
  })
  // auto emit result
  if (autoApply.value) {
    applyResult()
  }
}

const emit = defineEmits(['input', 'hide'])

const applyResult = () => {
  let resultNotNumber = Number.isNaN(Number.parseInt(expression.value))
  console.log('input', resultNotNumber ? '0' : expression.value)
  emit('result', resultNotNumber ? '0' : expression.value)
  hideInterface()
}
const hideInterface = () => {
  emit('hide')
  // hide styles only after playing the animation
  // TODO bad! We need to find a way out!
  setTimeout(() => {
    showStyles.value = false
  }, 500)
}
const clear = () => {
  expression.value = '0'
  isResult.value = false
}
</script>

<style lang="scss" scoped>
*,
::after,
::before {
  box-sizing: border-box;
}

.calculator-container {
  z-index: 0;
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Chrome/Safari/Opera */
  -khtml-user-select: none; /* Konqueror */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently not supported by any browser */

  .calc-wrapper {
    padding: 0;
    position: fixed;
    bottom: 0;
    z-index: 1;

    .calculator {
      width: 100%;
      display: flex;
      margin: 0 auto;
      flex-direction: column;
      max-width: 720px;
      min-width: 320px;
      background-color: var(--calculator-container-bg-color);
      box-shadow: 0 0 0 1px var(--calculator-container-bg-color);

      .calculator-logs {
        padding: 0 0.8rem 0 0.8rem;
        max-height: 100px;
        display: flex;
        position: relative;
        overflow: auto;
        align-items: flex-end;
        flex-direction: column;
        background: var(--calculator-container-event-btn-bg-color);

        .header {
          color: var(--calculator-container-text-color);
          align-self: flex-start;
          position: sticky;
          top: 0;
          left: 0;
          padding-top: 5px;
        }

        span {
          color: var(--calculator-container-text-color);
          opacity: 0.75;
          display: block;
          font-size: 1rem;
          text-align: right;
          padding: 0.4rem 0;
          line-height: 1;
          font-weight: lighter;
        }
      }

      .calculator-input {
        color: var(--calculator-container-text-color);
        width: 100%;
        border: none;
        padding: 0.8rem;
        display: block;
        font-size: 2.4rem;
        background: none;
        text-align: right;
        font-weight: lighter;

        &:focus,
        &:active {
          outline: none;
        }
      }

      .calculator-row {
        display: flex;
        padding: 0;
        justify-content: space-around;

        .calculator-col {
          flex: 1;
          box-shadow: 0 0 0 1px var(--calculator-container-bg-color);

          &.wide {
            flex: 2;
          }
        }
      }

      .calculator-btn {
        width: 100%;
        color: var(--calculator-container-text-color);
        border: none;
        cursor: pointer;
        padding: 0.3rem;
        outline: none;
        font-size: 2rem;
        transition: all 0.3s ease-in-out;
        font-weight: 200;
        justify-content: center;
        background-color: var(--calculator-container-number-btn-bg-color);

        &.success {
          background-color: var(--calculator-container-action-success-btn-bg-color);
          color: var(--calculator-container-text-color);
        }

        &.accent {
          background-color: var(--calculator-container-action-btn-bg-color);
          color: var(--calculator-container-text-color);
        }

        &.gray {
          background-color: var(--calculator-container-event-btn-bg-color);
        }

        &.action {
        }

        &:active {
          background-color: var(--calculator-container-bg-color);
        }
      }
    }
  }

  // pad under the calculator
  .backdrop {
    background-color: rgba(0, 0, 0, 0.5);
    width: 100%;
    height: 100%;
    z-index: 0;
  }
}

// calculator movement animation
.slide-enter-active {
  animation: slide-in 0.5s;
}

.slide-leave-active {
  animation: slide-in 0.3s reverse;
}

@keyframes slide-in {
  from {
    transform: translateY(100%);
  }
  to {
    transform: translateY(0);
  }
}

// background transparency animation - backdrop
.opacity-enter-active {
  animation: opacity-in 0.5s;
}

.opacity-leave-active {
  animation: opacity-in 0.3s reverse;
}

@keyframes opacity-in {
  100% {
    opacity: 1;
  }
  0% {
    opacity: 0;
  }
}
</style>
