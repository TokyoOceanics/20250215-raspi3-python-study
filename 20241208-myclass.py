class MyClass:
    """A simple example class"""         # 三重クォートによるコメント

    def __init__(self,name="default"):                  # コンストラクタ
        #self.name = "default"

    def getName(self):                   # getName()メソッド
        return self.name

    def setName(self, name):             # setName()メソッド
        self.name = name

a = MyClass()                            # クラスのインスタンスを生成
a.setName("Tanaka")                      # setName()メソッドをコール
print(a.getName())                       # getName()メソッドをコール

b=MyClass()
print(b.getName())