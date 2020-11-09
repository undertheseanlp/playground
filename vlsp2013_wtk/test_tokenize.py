from vlsp2013_wtk.regex_tokenize import tokenize as pure_tokenize

f = open("../data/UNEWS-100K-V1.txt")
text = 'Còn ngư dân thì còn bám biển, ông Trọng khẳng định. Tp. ... => =))) http://abc.com abc.com@gmail.com #abcajla 10 10.20 100,200,300 10h20 10:20 20/10 20-10-2020 10/1995 '
text = 'Ông được bổ nhiệm vị trí Giám đốc Sở TN&MT; Yên Bái từ ngày 9/9/2016. H&M'
text = 'Cuối cùng Ban giám khảo đã chấm ba giải A trang trí mâm ngũ quả, gồm: PA65, PA72 và PV24; ba giải A trang trí mâm cỗ thuộc về PX14, PC67 và Báo CATP.HCM; ngoài ra BTC còn trao 6 giải B và 6 giải C cho các đội dự thi.'
text = 'Quay phim :Dương Tuấn Anh Diễn viên : :D :D'
text = 'Tiêm kích F-16 Bỉ bám sát, dùng cảm biến ảnh nhiệt để chụp ảnh tiêm kích bom Su-34 Nga trên không phận quốc tế ở biển Baltic'
text = 'Tai nạn, do tài xế điều khiển xe Lexus biển kiểm soát 49X-6666 khiến 4 người tử vong và 6 người bị thương nặng'
text = 'T-ara  K-pop J-pop C-pop'
text = 'Toàn cảnh lễ ký kết giữa công ty Tân Thạnh A và công ty Lotte E&C'
text = 'Tầm giá quá rẻ để mua 1 cục bực tức để trên người :)) Rolls-Royce'
text = '(baodautu.vn) Trao đổi với báo chí chiều 27/5, ông Lê Quốc Bình, TGĐ Công ty cổ phần đầu tư hạ tầng kỹ thuật TP. HCM (CII) chính thức thông tin: UBND TP vừa có quyết định cho phép CII được thu phí hoàn vốn đầu tư dự án xây dựng cầu Rạch Chiếc mới trên xa lộ Hà Nội kể từ ngày 1/6/2013.'
tokens = pure_tokenize(text)
for token in tokens:
    print(token)
# tokens2 = tokenize(text)