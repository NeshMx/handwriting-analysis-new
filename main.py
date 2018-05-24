from sklearn import datasets
from sklearn.svm import SVC
import scipy.misc as misc
from os import environ
environ['SCIPY_PIL_IMAGE_VIEWER'] = '/usr/bin/eog'
# import login


def digits_recognition(fname):
    digits = datasets.load_digits()
    features = digits.data
    print(features)
    labels = digits.target
    print(labels)

    clf = SVC(gamma=0.001)
    clf.fit(features, labels)

    img = misc.imread(fname)
    misc.imshow(img)
    img = misc.imresize(img, (8, 8))
    misc.imshow(img)
    img = img.astype(digits.images.dtype)
    img = misc.bytescale(img, high=16, low=0)

    x_test = []

    for eachRow in img:
        for eachPixel in eachRow:
            x_test.append(sum(eachPixel)/3.0)

    print('Numero: ')
    print(clf.predict([x_test]))


def main():
    fname = input('Introduce la ruta del archivo: ')
    digits_recognition(fname)


if __name__ == '__main__':
    main()
