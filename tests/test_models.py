from resnext_keras.models import ResNext

if __name__ == '__main__':
    model = ResNext((32, 32, 3), depth=29, cardinality=8, width=64)
    model.summary()
