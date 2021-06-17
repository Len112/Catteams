-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 17, 2021 at 06:15 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.2.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `catteams`
--

-- --------------------------------------------------------

--
-- Table structure for table `tcompany`
--

CREATE TABLE `tcompany` (
  `idcompany` int(2) NOT NULL,
  `namecompany` text NOT NULL,
  `emailcompany` text NOT NULL,
  `nomorcompany` text NOT NULL,
  `alamatcompany` text NOT NULL,
  `photocompany` text NOT NULL,
  `aboutcompany` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tcompany`
--

INSERT INTO `tcompany` (`idcompany`, `namecompany`, `emailcompany`, `nomorcompany`, `alamatcompany`, `photocompany`, `aboutcompany`) VALUES
(1, 'Cat Teams', 'ellenpr011200@gmail.com', '087644628345', 'Jalan Panturan nomor 50', 'yo.jpg', 'Perusahaan Nirlaba untuk komunitas pecinta kucing');

-- --------------------------------------------------------

--
-- Table structure for table `tkucing`
--

CREATE TABLE `tkucing` (
  `idkucing` int(11) NOT NULL,
  `namakucing` varchar(255) NOT NULL,
  `jeniskucing` varchar(255) NOT NULL,
  `usiakucing` varchar(10) NOT NULL,
  `ukurankucing` varchar(10) NOT NULL,
  `jeniskelamin` varchar(255) NOT NULL,
  `photokucing` varchar(255) NOT NULL,
  `tentangkucing` text NOT NULL,
  `statuskucing` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tkucing`
--

INSERT INTO `tkucing` (`idkucing`, `namakucing`, `jeniskucing`, `usiakucing`, `ukurankucing`, `jeniskelamin`, `photokucing`, `tentangkucing`, `statuskucing`) VALUES
(1, 'Sirec', 'Domestica', 'Kitten', 'Small', 'Perempuan', 'kucing.jpg', 'Health : not vaccinated', 'Telah di Adopsi'),
(2, 'Jeremy', 'Domestica', 'Adult', 'Medium', 'Laki-Laki', 'Kucing1.jpg', 'Health : not vaccinated', 'Proses Adopsi'),
(3, 'Dallas', 'Domestica', 'Senior', 'Large', 'Laki-Laki', '369010003p.jpg', 'Health : Have been vaccinated', 'Siap di Adopsi'),
(4, 'Vivian', 'Persia', 'Kitten', 'Small', 'Perempuan', 'anak.jpg', 'Sudah di vaksin, suka main laser, suka makan ikan asin, suka main bola', 'Siap di Adopsi'),
(5, 'Sunshine', 'Anggora', 'Senior', 'Large', 'Laki-Laki', '5dbfff829ebe6.jpg', 'Sudah di kebiri, sudah divaksin', 'Proses Adopsi'),
(6, 'Niken', 'Persia', 'Adult', 'Medium', 'Perempuan', 'images (1).jpg', 'Sudah di vaksin, suka makan  ikan asin, datang kalau di panggil', 'Proses Adopsi'),
(7, 'Cosmix', 'Anggora', 'Senior', 'Large', 'Laki-Laki', 'jack.jpg', 'Sudah di vaksin, mata warna berbeda dan suka tiduran', 'Proses Adopsi'),
(8, 'Hana', 'RagDoll', 'Adult', 'Medium', 'Perempuan', 'ragdoll.jpg', 'Belum di vaksin, belum dikebiri,  bulu halus, suka sekali bermain dengan bebek karet', 'Siap di Adopsi'),
(9, 'Grey', 'Britania', 'Adult', 'Large', 'Laki-Laki', 'images.jpg', 'Kucing sudah divaksin, sudah di kebiri, pendiam, gembul', 'Siap di Adopsi'),
(10, 'Noira', 'Siam', 'Adult', 'Medium', 'Perempuan', 'siam.jpg', 'Sudah di vaksin, hanya makan tuna kaleng', 'Siap di Adopsi'),
(11, 'SiGundul', 'PeterBald', 'Senior', 'Large', 'Perempuan', 'Peterbald.jpg', 'Sudah divaksin, sudah dikebiri, bisa makan apa saja yang diperbolehkan kucing', 'Siap di Adopsi'),
(13, 'Jian', 'Persia', 'Kitten', 'Small', 'Perempuan', 'images (2).jpg', 'Baru lahir, agresif', 'Telah di Adopsi'),
(14, 'Cities', 'Anggora', 'Kitten', 'Small', 'Laki-Laki', 'kugj.jpg', 'Pendiam, sudah divaksin', 'Siap di Adopsi'),
(15, 'BonnieFis', 'PeterBalds', 'Kitten', 'Medium', 'Perempuan', 'download.jpg', 'Kucing baru lahir', 'Siap di Adopsi'),
(16, 'Selena', 'Domestica', 'Kitten', 'Medium', 'Perempuan', 'images (4).jpg', 'Kucing pendiam', 'Siap di Adopsi');

-- --------------------------------------------------------

--
-- Table structure for table `tmessage`
--

CREATE TABLE `tmessage` (
  `idmessage` int(10) NOT NULL,
  `name` varchar(25) NOT NULL,
  `email` text NOT NULL,
  `subject` text NOT NULL,
  `message` longtext NOT NULL,
  `tanggal_kirim` datetime NOT NULL,
  `tanggal_dibalas` datetime NOT NULL,
  `replied` varchar(4) NOT NULL,
  `replymessage` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tmessage`
--

INSERT INTO `tmessage` (`idmessage`, `name`, `email`, `subject`, `message`, `tanggal_kirim`, `tanggal_dibalas`, `replied`, `replymessage`) VALUES
(1, 'Ellen', 'Ellen_pratama112@yahoo.com', 'Test', 'hai', '2021-05-07 05:28:18', '2021-05-09 22:25:24', 'Yes', 'Hai juga'),
(2, 'Ellen', 'Ellen.pratama.ep@gmail.com', 'Perkenalan', 'dasasa', '2021-05-07 14:19:19', '2021-05-07 23:12:21', 'Yes', 'saya'),
(3, 'Ellen', 'Ellen_pratama112@yahoo.com', 'Lima', 'Do you seee', '2021-05-07 10:00:00', '2021-05-09 22:32:21', 'Yes', 'saya juga melihat'),
(4, 'Nisa', 'Ellen_pratama112@yahoo.com', 'Perkenalan', 'Hallo', '2021-05-07 22:36:19', '2021-05-08 15:52:33', 'Yes', 'Haloo Haloo'),
(5, 'Nisa', 'Ellen.pratama.ep@gmail.com', 'Perkenalan', 'Halo', '2021-05-09 17:27:54', '2021-05-09 22:36:01', 'Yes', 'hallooo'),
(6, 'Yusuf', 'Ellen011200@gmail.com', 'Mengenai kucing Ku', 'Kucingku bulu nya rontok', '2021-05-09 17:29:18', '2021-06-17 13:34:55', 'Yes', 'Bulu kucing rontok bisa di sebabkan :\r\n1.1. Kondisi kulit kucing\r\n\r\nKucing dengan bulu yang kerap rontok mungkin saja mengalami infeksi seperti kurap kucing (infeksi jamur), infestasi parasit seperti tungau atau kutu, atau kondisi kulit kucing lain yang disebabkan oleh alergi. Karena semua hal ini akan mengiritasi kulit, kucing lantas akan sering menggaruk-garuk tubuhnya dan merontokkan sebagian besar bulunya. \r\n\r\n2. Stres atau nyeri\r\n\r\nTerkadang, kucing yang merasa stres dapat memicu kerontokan pada bulu-bulunya. Saat tubuhnya terasa sakit atau nyeri, kucing juga cenderung merawat area yang sakit tersebut dengan menjilatnya secara berlebihan, yang dapat menyebabkan bulu-bulu di sekitar area tersebut menjadi rontok.\r\n\r\n3. Hormon Kucing\r\n\r\nPada kucing, kebotakan dan bulu yang rontok juga bisa disebabkan oleh ketidakseimbangan hormon. Hormon tertentu bertanggung jawab atas pertumbuhan bulu kucing dan pada gilirannya, dapat menjadi alasan mengapa bulu kucing menjadi rontok.'),
(7, 'Bima', 'Ellen_pratama112@yahoo.com', 'cara mengetahui kucing sakit ?', 'Halo kak sesuai subject nih... Gimana sih cara mengetahui kucing sakit ?', '2021-05-09 22:35:26', '2021-06-17 22:09:51', 'Yes', 'Biasa nya kucing sakit itu tidak mau bergerak, dan bersembunya dan juga tidak mau makan '),
(8, 'Bima', 'Ellen_pratama112@yahoo.com', 'Perkenalan', 'HAI NAMA SAYA BIMA', '2021-06-17 00:43:31', '0000-00-00 00:00:00', 'No', ''),
(9, 'Ellen', 'Ellen.pratama.ep@gmail.com', 'Kucing yang tidak mau makan ', 'Halo saya ingin menanyakan tentang kucing saya dengan jenis persia, kucing saya sudah tidak mau makan dari 2 hari yang lalu. Saya bingung apa penyebabnya bisa beri saran ?', '2021-06-17 16:08:29', '2021-06-17 16:10:10', 'Yes', ', kucing kakak mungkin kurang menyukai makanan yang kakak berikan. Atau jika dia tidak banyak bergerak dan terasa lesu kemungkinan dia sakit. Segera bawa dia kedokter hewa terdekat kak'),
(10, 'Ellen', 'Ellen.pratama.ep@gmail.com', 'Mengenai kucing ku yang  jarang makan', 'Hai,, saya ingin bertanya mengenai kucing ku yang jarang makan... kira-kira bisa beri masukan agar kucing ku mau makan  ?', '2021-06-17 22:08:53', '0000-00-00 00:00:00', 'No', '');

-- --------------------------------------------------------

--
-- Table structure for table `tpengadopsi`
--

CREATE TABLE `tpengadopsi` (
  `idadopsi` varchar(8) NOT NULL,
  `noidentitaspengadopsi` varchar(20) NOT NULL,
  `namapengadopsi` varchar(255) NOT NULL,
  `emailpengadopsi` varchar(255) NOT NULL,
  `teleponpengadopsi` varchar(255) NOT NULL,
  `jeniskelamin` varchar(255) NOT NULL,
  `alamatpengadopsi` varchar(255) NOT NULL,
  `alasanadopsi` text NOT NULL,
  `statusadopsi` varchar(20) NOT NULL,
  `idkucing` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tpengadopsi`
--

INSERT INTO `tpengadopsi` (`idadopsi`, `noidentitaspengadopsi`, `namapengadopsi`, `emailpengadopsi`, `teleponpengadopsi`, `jeniskelamin`, `alamatpengadopsi`, `alasanadopsi`, `statusadopsi`, `idkucing`) VALUES
('0K8791LU', '123456789012345', 'Ellen', 'Ellen.pratama.ep@gmail.com', '08787732313134', 'Perempuan', 'Jelambar barat', 'Iseng', 'Adopsi ditolak', 3),
('8UE5F52F', '12345672829001', 'Ellen', 'Ellen_pratama112@yahoo.com', '087233456273', 'Perempuan', 'Jalan Ujung utara nomor 18', 'Karena suka memelihara kucing', 'Adopsi diterima', 2),
('BUBYTMOV', '123456789012345', 'Ellen', 'Ellen.pratama.ep@gmail.com', '087877297023', 'Perempuan', 'Jelambar barat', 'Menyukai kucing', 'Adopsi Berhasil', 1),
('JXLBFP6Y', '111222333444555', 'Ellen', 'Ellen.pratama.ep@gmail.com', '089656193224', 'Perempuan', 'Jalan Gambir nomor 34', 'Suka sekali kucing', 'Adopsi ditolak', 6),
('STCWLPKE', '123456789012345', 'Ellen', 'Ellen.pratama.ep@gmail.com', '0878772987314', 'Perempuan', 'Jelambar barat', 'Suka kucing', 'Proses Pengajuan', 5),
('YZJ623MV', '313234555634422', 'Ellen', 'Ellen.pratama.ep@gmail.com', '087455647283445', 'Perempuan', 'Jalan Gilang nomor 34', 'Karena suka kucing', 'Proses Pengajuan', 6);

--
-- Triggers `tpengadopsi`
--
DELIMITER $$
CREATE TRIGGER `statuskucing` AFTER INSERT ON `tpengadopsi` FOR EACH ROW BEGIN
UPDATE tkucing SET tkucing.statuskucing = "Proses Adopsi" WHERE tkucing.idkucing = NEW.idkucing ;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tsubscribe`
--

CREATE TABLE `tsubscribe` (
  `idsubscribe` int(11) NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tsubscribe`
--

INSERT INTO `tsubscribe` (`idsubscribe`, `email`) VALUES
(1, 'ellen.pratama.ep@gmail.com'),
(2, 'Ellen_pratama112@yahoo.com'),
(3, 'pratamaell112@gmail.com'),
(4, 'Ellen011200@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `tteam`
--

CREATE TABLE `tteam` (
  `idteam` int(10) NOT NULL,
  `namateam` varchar(30) NOT NULL,
  `jeniskelamin` varchar(20) NOT NULL,
  `nomorhp` varchar(20) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `jabatan` varchar(15) NOT NULL,
  `userid` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tteam`
--

INSERT INTO `tteam` (`idteam`, `namateam`, `jeniskelamin`, `nomorhp`, `alamat`, `jabatan`, `userid`) VALUES
(1, 'Joseph Surkan', 'Laki-Laki', '089656108321', 'Jalan simatupang nomor 2', 'Manager', 'Joseph134'),
(2, 'Ujang', 'Laki-Laki', '087877297863', 'Jalan simatupang nomor 10', 'Contributor', 'Ujang245'),
(3, 'Nikki', 'Perempuan', '087877297023', 'Jalan simatupang nomor 10', 'Executive', 'Nikki367'),
(4, 'Dian', 'Perempuan', '08746646327', 'Jalan Gatot nomor 3', 'Manager', 'Dian425'),
(5, 'Winnie', 'Perempuan', '089656108322', 'Jalan Nihab I nomor 5', 'Executive', 'Winnie587'),
(6, 'EllenPr', 'Perempuan', '087877297027', 'Jalan simatupang nomor 7', 'Executive', 'Ellen612'),
(7, 'Susi susanti', 'Perempuan', '08654241022', 'Jalan Nihab I nomor 5', 'Executive', 'Susi791'),
(8, 'Fiera Anastasya', 'Perempuan', '08932888382291', 'Jalan Timur Barat 5 nomor 56', 'Contributor', 'FieraAnastasya816'),
(9, 'Cintaanastasia', 'Perempuan', '09127834566', 'Jalan jalan utama nomor 50', 'Contributor', 'Cintaanastasia92');

-- --------------------------------------------------------

--
-- Table structure for table `tuser`
--

CREATE TABLE `tuser` (
  `userid` varchar(100) NOT NULL,
  `userpassword` longtext NOT NULL,
  `userphoto` varchar(1000) NOT NULL,
  `hakakses` varchar(15) NOT NULL,
  `username` varchar(30) NOT NULL,
  `userabout` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tuser`
--

INSERT INTO `tuser` (`userid`, `userpassword`, `userphoto`, `hakakses`, `username`, `userabout`) VALUES
('Cintaanastasia92', 'pbkdf2:sha256:150000$1erOTMuQ$65d54d75f7540c2753db31480ceb18d5c5aa0595615611af73a0c8f9f32e173f', 'Luna.jpg', 'Contributor', 'Cintaanastasia', 'Tuliskan tentang diri anda'),
('Dian425', 'pbkdf2:sha256:150000$8jZLuoC0$dcafa9b679e306b0d736594058eaa693bd74755928a3e7909feab5ea08ddf3fc', 'Aili.png', 'Manager', 'Dian Permata', 'Santai'),
('Ellen612', 'pbkdf2:sha256:150000$Ir7n1tyH$9379a991e7eccb94c501014018bb02987c7cbb4ec77a55c20a0f745c7320f084', 'pp2.jpeg', 'Executive', 'EllenPr', '\"You can\'t connect the dots looking forward; you can only connect them looking backward. So you have to trust that the dots will somehow connect in your future\"'),
('FieraAnastasya816', 'pbkdf2:sha256:150000$9pvdxRDd$96143c6add6331ac9496e799ce952c569635fffad075f334918699e26f5554ed', 'Nissa.jpg', 'Contributor', 'Fiera Anastasya', ''),
('Joseph134', 'pbkdf2:sha256:150000$sR8zDuui$37cb5b08568b78f8324b4729a58a49c8fb7bba69d7102830f9ead33c1c11007c', 'Jiminuwu.jpg', 'Manager', 'Joseph Surkan', ''),
('Nikki367', 'pbkdf2:sha256:150000$sR8zDuui$37cb5b08568b78f8324b4729a58a49c8fb7bba69d7102830f9ead33c1c11007c', 'Jiminuwu.jpg', 'Executif', 'Nikki', 'Life is never flat'),
('Susi791', 'pbkdf2:sha256:150000$Hh8GHCVS$c9378323fd8d564bf0d68e1d1418c8a7cfa86206e303cff7f819409c53cadff0', 'fotopp.png', 'Executif', 'Susi susanti', 'Life is a journey to be experienced, not a problem to be solved'),
('Ujang245', 'pbkdf2:sha256:150000$sR8zDuui$37cb5b08568b78f8324b4729a58a49c8fb7bba69d7102830f9ead33c1c11007c', 'pic-1.png', 'Contributor', 'Ujang', ''),
('Winnie587', 'pbkdf2:sha256:150000$sR8zDuui$37cb5b08568b78f8324b4729a58a49c8fb7bba69d7102830f9ead33c1c11007c', 'Fotoku.jpg', 'Executif', 'Winnie', 'Do something today that your future self will thank you for');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tcompany`
--
ALTER TABLE `tcompany`
  ADD PRIMARY KEY (`idcompany`);

--
-- Indexes for table `tkucing`
--
ALTER TABLE `tkucing`
  ADD PRIMARY KEY (`idkucing`);

--
-- Indexes for table `tmessage`
--
ALTER TABLE `tmessage`
  ADD PRIMARY KEY (`idmessage`);

--
-- Indexes for table `tpengadopsi`
--
ALTER TABLE `tpengadopsi`
  ADD PRIMARY KEY (`idadopsi`);

--
-- Indexes for table `tsubscribe`
--
ALTER TABLE `tsubscribe`
  ADD PRIMARY KEY (`idsubscribe`);

--
-- Indexes for table `tteam`
--
ALTER TABLE `tteam`
  ADD PRIMARY KEY (`idteam`);

--
-- Indexes for table `tuser`
--
ALTER TABLE `tuser`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tcompany`
--
ALTER TABLE `tcompany`
  MODIFY `idcompany` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tkucing`
--
ALTER TABLE `tkucing`
  MODIFY `idkucing` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `tmessage`
--
ALTER TABLE `tmessage`
  MODIFY `idmessage` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tsubscribe`
--
ALTER TABLE `tsubscribe`
  MODIFY `idsubscribe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tteam`
--
ALTER TABLE `tteam`
  MODIFY `idteam` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
