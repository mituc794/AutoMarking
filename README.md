Đặt bài làm vào thư mục 'a'

Chạy main.py để bắt đầu.

Thay đổi tham số x,y,w,h trong get_points.py tương ứng với tọa độ góc trên trái của khu vực tô đáp án.

Thay đổi tham số x_i, y_i, w_i, h_i trong getID.py tương ứng với tọa độ góc trên trái của khu vực tô số báo danh. 

Dùng getID.ID_map_test(test_image=True) để xem vị trí các ô đúng hay chưa, nếu chưa thì thay đổi lại thủ công (tính năng định vị ô tự động đang được phát triển). Kết quả lưu trong map/res_mapping.

Sửa dòng 
    print('Diem cua '+getID.getID('a/'+file_name)+' la: ', len(matching_dots))
trong main.py để lưu file tùy nhu cầu.

Thay đổi dst_src trong
    img_process.img_process(key_dot_list, 'a/'+file_name, 'b/')
thành getID để lưu file ảnh đã chấm theo ID

Ảnh đã chấm được lưu vào thư mục 'b'
