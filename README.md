# Hotel Reservation System Using ( Python Django - Mysql  )

<h3>Senaryo : </h3>
Bir Otel otomasyonu yazılımı ve oda otomasyonu online olarak birlikte tam entegre halde çalışmakta ve oda rezervasyon durumunda bir değişiklik olduğunda hazır hale gelmesi bir Uygulama programı, veritabanı ve arayüzü tasarlandı.
Tasarlanan veritabanında müşteriler, oteller, odalar, rizervasyonlar, otelde çalışan elemanlar vb. bilgilerin saklanıyor.


### İlişkisel şeması: 
+	guest (GuestID :  bigint, FirstName: varchar(45), LastName: varchar(45))
+	hotel (HotelID: mediumint, HotelName: text, HotelImage: text, Hotelrate: int)
+	reservation (ReservationID: bigint, Guest_GuestID: bigint)
+	reservationdetail  ( ReservationDetailID: bigint, Reservation_ReservationID: bigint, RoomReservation_RoomReservationID: bigint, Description: varchar(45))
+	reservationpromo (Promo_PromoID: bigint, Reservation_ReservationID: bigint)
+	roomrate ( RoomRateID: bigint, RoomType_RoomTypeID: smallint,  PRIMARY)
+	roomtype (RoomTypeID: smallint,RoomType: varchar(20))
+	roomreservationguest (Guest_GuestID: bigint, RoomReservation_RoomReservationID: bigint)
+	promo ( PromoID: bigint, PromoCode: varchar(20),  Description  varchar(45),  RoomType_RoomTypeID: smallint)
+	roomreservation ( RoomReservationID: bigint, Room_RoomID: int, Reservation_ReservationID: bigint)
+	room ( RoomID: int, RoomType_RoomTypeID: smallint, Hotel_HotelID: mediumint)
+	hotelemployee ( Hotel_HotelID: mediumint, Employee_EmployeeID: bigint)
+	employee ( EmployeeID: bigint, FirstName: varchar(45), LastName: varchar(45))

<h3>Use Case Diagramı :</h3>
![alt text](https://github.com/nermiin/hotelbooking/blob/master/images/use_case.png "Use Case Diagram")
