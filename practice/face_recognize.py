import cv2


def face_recognition(filepath: str):
    img: cv2.typing.MatLike = cv2.imread(filepath)

    # 转换灰色
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 人脸模型地址
    add = r'D:\DevTools\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'

    classifier = cv2.CascadeClassifier(add)
    color = (0, 255, 0)  # 定义绘制颜色

    # 调用识别人脸
    '''
    使用 cv2.CascadeClassifier.detectMultiScale() 方法进行人脸检测。该方法返回检测到的人脸区域的矩形框（x, y, w, h），
    其中 (x, y) 是矩形框的左上角坐标，w 和 h 分别是矩形框的宽度和高度。
    
    scaleFactor: 表示每次图像尺寸减小的比例，用于构建图像金字塔。默认值为 1.1。 可理解为相机的X倍镜
    minNeighbors: 表示每个候选矩形框应该保留的邻居数量。默认值为 5,
    对特征检测点周边多少有效点同时检测，这样可避免因选取的特征检测点太小而导致遗漏
    minSize: 表示检测目标的最小尺寸。默认值为 (30, 30)。
    '''
    faceRects = classifier.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

    if len(faceRects):  # 大于0则检测到人脸
        for faceRect in faceRects:  # 单独框出每一张人脸
            x, y, w, h = faceRect
            # 框出人脸
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            # 左眼
            cv2.circle(img, (x + 5 * w // 16, y + 6 * h // 16), min(w // 8, h // 8),
                       color)
            # 右眼
            cv2.circle(img, (x + 11 * w // 16, y + 6 * h // 16), min(w // 8, h // 8),
                       color)
            # 嘴巴
            cv2.rectangle(img, (x + 5 * w // 16, y + 11 * h // 16),
                          (x + 11 * w // 16, y + 14 * h // 16), color)

    cv2.imshow("image", img)  # 显示图像
    c = cv2.waitKey(10)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # filepath = r'../img/xingye-2.png'
    # filepath = r'C:\Users\69152\Pictures\R-C.jpg'
    # filepath = r'D:\Personal\Identification Photo\0254230335.jpg'
    # filepath = r'D:\Personal\Identification Photo\330327200105183739.jpg'
    # filepath = r'D:\Personal\Identification Photo\1744453146315.jpg'
    # filepath = r'D:\Personal\Materials\R-C.jpg'
    # filepath = r'D:\Personal\Materials\R-C1.jpg'
    filepath = r'D:\Personal\Materials\FaceTidyup5.png'
    face_recognition(filepath)
