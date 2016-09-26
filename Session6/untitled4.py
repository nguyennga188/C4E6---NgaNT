from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

class film:
    def __init__(self, name, info, img, link):
        self.name = name
        self.info = info
        self.img = img
        self.link = link

film1 = film(
    "Train to Busan",
    "Train To Busan - Chuyến Tàu Sinh Tử 2016 lấy bối cảnh đất nước Hàn bị tấn công bởi một loại virus bí ẩn, biến con người thành những xác sống hung hăng, khát máu. Có mặt trên chuyến tàu từ Seoul tới Busan là một người cha cùng con gái, hai vợ chồng chuẩn bị đón đứa con đầu lòng và một số cô cậu học sinh cấp 3. Khi đại dịch xác sống bất ngờ bùng phát, họ không còn cách nào khác ngoài đương đầu với nó để bảo vệ những người thân yêu của mình. Hành trình 453km từ Seoul tới vùng an toàn Busan bỗng trở thành cuộc chiến khốc liệt để sinh tồn.",
    "http://image-us.24h.com.vn/upload/3-2016/images/2016-08-15/1471225342-147116173415208-1469159574-146915918022813-chuyentausinhtu--4-.jpg",
    "http://hdonline.vn/phim-chuyen-tau-sinh-tu-12648.html"
)

film2 = film(
    "Moonlight drawn by clouds",
    "Phim Mây Họa Ánh Trăng - Love in the Moonlight (2016): Hong Ra-On cải trang thành đàn ông để tìm lời khuyên ở đàn ông về việc hẹn hò. Cũng vì một bức thư tình mà cô viết cho một vị khách mà cô gặp thái tử Hyomyeong. Hong Ra-On không hề biết người này là hoàng tử và Hyomyeong cũng không biết Hong Ra-On là phụ nữ. Thái tử dần dần có cảm tình với Hong Ra-On. ",
    "http://www.jauhari.net/engine/wp-content/uploads/2016/07/moonlight-4.jpg",
    "http://phimbathu.com/may-hoa-anh-trang-3681.html"
)

film3 = film(
    "THE SECRET LIFE OF PETS (2016)",
    "Phim Đẳng Cấp Thú Cưng (2016): Chuyện phim lấy bối cảnh một khu chưng cư giữa Manhattan náo nhiệt, phồn vinh – nơi các thú cưng thường có nhiều thời gian rảnh sau khi chủ rời nhà đi làm. Thay vì thấy cô đơn, chúng coi đây là cơ hội để hưởng thụ cuộc sống, tận hưởng cảm giác vương giả trong ngôi nhà rộng lớn.",
    "http://static.phimnhanh.com/Thanh/dang-cap-thu-cung-the-secret-life-of-pets-2016/the-secret-life-of-pets-2016-hd.jpg",
    "http://hdonline.vn/phim-the-secret-life-of-pets-8882.html"
)

films = [film1, film2, film3]

@app.route('/fav')
def fav():
    return render_template("fav.html", films=films)

@app.route('/fav/<int:index>')
def fav1(index):
    if index not in range(len(films)):
        return "<h1>film not found</h1>"
    return render_template("fav1.html", film=films[index])


if __name__ == '__main__':
    app.run()
