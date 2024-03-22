# 파이썬의 객체지향 언어 특징
# 1. 다중상속을 지원
# 2. 캡슐화(접근제한자)는 제대로 지원 되지 않음
# 3. 다형성에서 오버라이딩은 지원, 오버로딩은 지원 하지 않음(데이터의 타입이 없고, 디폴트 매개변수를 지원)
# 4. 생성자 키워드 : __init__
# 5. 자바에서 말하는 인스턴스 필드는 생성자 내에 존재해야 함
# 6. 자신의 객체를 가리키는 포인터는 생성자 또는 매소드의 첫번째 인자임(관례상 self이름 사용)
class TV:
    def __init__(self, name, is_on, channel, volume):
        self.name = name
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on):
        self.is_on = is_on
    def set_channel(self, cnl):
        self.channel = cnl
    def set_volume(self, vol):
        self.volume = vol
    def get_on(self):
        return self.is_on
    def get_channel(self):
        return self.channel
    def get_volume(self):
        return self.volume
    def view_tv(self):
        power = "OFF", "ON"
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

lg_tv = TV("LG", False, 10, 10)
sam_tv = TV("삼성", True, 20, 20)
lg_tv.view_tv()
sam_tv.view_tv()