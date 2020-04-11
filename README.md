# report-week
#Báo cáo ngày 12-4-2020

##1. Tạo topo bằng mininet-wifi:
- Topo bao gồm: 1 host(h0), 1 Controller(s0), 2 accespoint(ap1,ap2), 1 station(sta0).
- Accesspoint: Thiết bị thu phát wifi, ngoài ra còn là điểm kết nối mạng WLan và mạng dây cố định.
- Station: Thiết bị kết nối với AP thông qua xác thực và liên kết, mỗi station có 1 wireless card(StaX-Wlan0,X là số hiệu của mỗi station).
- Các câu lệnh: 
 - add.Host(), add.Link(), add.Accesspoint(),add.link(), add.Switch.
 - Mở topo default: sudo mn --wifi.
 - Xóa phiên trước: sudo mn --wifi -c.
 - Topo 1 AP, 5STA: sudo mn --wifi --test pingall --topo single,5.
 - Topo mỗi AP có 1 STA: sudo mn --wifi --test pingall --topo linear,5.
 - Mở topo tự tạo: sudo python file.py.
 - Tạo host: h1=net.addHost('h1',mac='',ip='')
 - Tạo AP: ap1=net.addAccesspoint('ap1',ssid='',mode='',channel='',position='')
 - Kiểm tra khoảng cách giữa 2 nodes: mininet>distance ap1 ap2
- Bắn iperf để kiểm tra băng thông: 
  - Sever: iperf -s
  - Client: iperf -c -u 'ip server'

##2.Vấn đề gặp phải: 
- h0 không ping được đến sta0:
 - h0 ping được đến ap1 và ap2.
 - ap1 và ap2 không ping được tới sta0.

##3.Tổng hợp lại về git,github:
- git .init: tạo local repo(note: tạo được nhiều repo)
- git add: đẩy những file vào staging(staging là nơi chứa những file đã sẵn sàng được commit đẩy vào repo.) 
- git stage. : Đẩy file được thay đổi vào staging
- git commit -m "": Đẩy vào local repo.
- git log: file đã commit vào local repo.
- git checkout <branch>: đổi branch muốn đẩy vào.
- git pull: đồng bộ repo trên github và local repo.




 
