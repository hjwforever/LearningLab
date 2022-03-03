class MsgCenter {
  constructor() {
    this.subscribers = []
  }
  register(subscribers) {
    if (Array.isArray(subscribers)) {
      subscribers.forEach(subscriber => this.subscribers.push(subscriber))
    } else {
      this.subscribers.push(subscribers)
    }
  }
  unRegister(id) {
    this.subscribers.splice(this.subscribers.findIndex(subscriber => subscriber.id == id),1)
  }
  onMsg(msg) {
    this.subscribers.forEach((subscriber) => {
      subscriber.onMsg(msg);
    })
  }
}

class Publisher {
  constructor(msgCenter) {
    this.msgCenter = msgCenter;
  }
  post(msg) {
    this.msgCenter.onMsg(msg);
  }
}

class Subscriber {
  constructor(id) {
    this.id = id ?? Math.random() * 100000;
  }
  onMsg(msg) {
    console.log(`user ${this.id} receives message: ${msg}`);
  }
}

const msgCenter = new MsgCenter()
const publisher = new Publisher(msgCenter)
const subscriber1 = new Subscriber(1)
const subscriber2 = new Subscriber(10086)

// test
msgCenter.register([subscriber1, subscriber2])
publisher.post('ss')
msgCenter.unRegister(1)
publisher.post('hh')