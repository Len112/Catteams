-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 08, 2021 at 08:29 AM
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
(1, 'Cat Teams', 'pratamaell112@yahoo.com', '087644628345', 'Jalam Utara selatan Nomor 5', 'yo.jpg', 'Non-Profit Company for cat lover community');

-- --------------------------------------------------------

--
-- Table structure for table `tkucing`
--

CREATE TABLE `tkucing` (
  `idkucing` int(11) NOT NULL,
  `namakucing` varchar(255) NOT NULL,
  `jeniskucing` varchar(255) NOT NULL,
  `jeniskelamin` varchar(255) NOT NULL,
  `photokucing` varchar(255) NOT NULL,
  `tentangkucing` text NOT NULL,
  `statuskucing` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(6, 'Yusuf', 'Ellen011200@gmail.com', 'Mengenai kucing Ku', 'Kucingku bulu nya rontok', '2021-05-09 17:29:18', '0000-00-00 00:00:00', 'No', ''),
(7, 'Bima', 'Ellen_pratama112@yahoo.com', 'cara mengetahui kucing sakit ?', 'Halo kak sesuai subject nih... Gimana sih cara mengetahui kucing sakit ?', '2021-05-09 22:35:26', '0000-00-00 00:00:00', 'No', '');

-- --------------------------------------------------------

--
-- Table structure for table `tpengadopsi`
--

CREATE TABLE `tpengadopsi` (
  `idpengadopsi` int(11) NOT NULL,
  `namapengadopsi` varchar(255) NOT NULL,
  `jeniskelamin` varchar(255) NOT NULL,
  `teleponpengadopsi` varchar(255) NOT NULL,
  `emailpengadopsi` varchar(255) NOT NULL,
  `alamatpengadopsi` varchar(255) NOT NULL,
  `alasanadopsi` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(2, 'Ellen_pratama112@yahoo.com');

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
(6, 'EllenPr', 'Perempuan', '087877297027', 'Jalan simatupang nomor 6', 'Executive', 'Ellen612'),
(7, 'Susi susanti', 'Perempuan', '08654241022', 'Jalan Nihab I nomor 5', 'Executive', 'Susi791'),
(8, 'Fiera Anastasya', 'Perempuan', '08932888382291', 'Jalan Timur Barat 5 nomor 56', 'Contributor', 'FieraAnastasya816');

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
('Dian425', 'pbkdf2:sha256:150000$8jZLuoC0$dcafa9b679e306b0d736594058eaa693bd74755928a3e7909feab5ea08ddf3fc', 'Aili.png', 'Manager', 'Dian Permata', 'Santai'),
('Ellen612', 'pbkdf2:sha256:150000$Ir7n1tyH$9379a991e7eccb94c501014018bb02987c7cbb4ec77a55c20a0f745c7320f084', 'pp2.jpeg', 'Executif', 'EllenPr', '\"You can\'t connect the dots looking forward; you can only connect them looking backward. So you have to trust that the dots will somehow connect in your future\"'),
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
  ADD PRIMARY KEY (`idpengadopsi`);

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
  MODIFY `idkucing` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tmessage`
--
ALTER TABLE `tmessage`
  MODIFY `idmessage` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tpengadopsi`
--
ALTER TABLE `tpengadopsi`
  MODIFY `idpengadopsi` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tsubscribe`
--
ALTER TABLE `tsubscribe`
  MODIFY `idsubscribe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tteam`
--
ALTER TABLE `tteam`
  MODIFY `idteam` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
