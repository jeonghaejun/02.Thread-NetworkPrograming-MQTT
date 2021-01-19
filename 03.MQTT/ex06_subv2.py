from mqtt_sub import subscribe
from datetime import datetime
from app_base import Application

class MonitorApp(Application):
    def __init__(self):
        super().__init__()
        subscribe('localhost', 'iot/#', self.on_message, forever=False)
        self.sensors = {
            'temp': [],
            'humi': [],
            'illu': [],
            'dust': [],
        }

    def create_menu(self, menu):
        menu.add('온도', self.print_temp)
        menu.add('습도', self.print_humi)
        menu.add('조도', self.print_illu)
        menu.add('미세먼지', self.print_dust)
        menu.add('종료', self.exit)

    def on_message(self, client, userdata, msg):
        with open(self.config.fname, 'at')as f:
            value = float(msg.payload)
            f.write(f'{datetime.now()},{msg.topic},{value}\n')
            key = msg.topic.split('/')[-1]
            self.sensors[key].append(value)

    def get_avg(self, key):
        total = sum(self.sensors[key])
        avg = total/len(self.sensors[key])
        return avg

    def print_temp(self):
        avg = self.get_avg('temp')
        print('평균 온도: ', avg)

    def print_humi(self):
        avg = self.get_avg('humi')
        print('평균 습도: ', avg)

    def print_illu(self):
        avg = self.get_avg('illu')
        print('평균 조도: ', avg)

    def print_dust(self):
        avg = self.get_avg('dust')
        print('평균 미세먼지: ', avg)


if __name__ == "__main__":
    app = MonitorApp()
    app.run()
