-- MariaDB dump 10.19  Distrib 10.6.5-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: parkco
-- ------------------------------------------------------
-- Server version	10.6.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `parkco`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `parkco` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `parkco`;

--
-- Temporary table structure for view `account`
--

DROP TABLE IF EXISTS `account`;
/*!50001 DROP VIEW IF EXISTS `account`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `account` (
  `email` tinyint NOT NULL,
  `username` tinyint NOT NULL,
  `password` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `idParkiran` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idParkiran` (`idParkiran`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`idParkiran`) REFERENCES `informasiparkiran` (`idParkiran`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `informasiparkiran`
--

DROP TABLE IF EXISTS `informasiparkiran`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `informasiparkiran` (
  `idParkiran` int(11) NOT NULL AUTO_INCREMENT,
  `namaParkiran` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `kapasitas` int(11) DEFAULT NULL,
  `slotTerisi` int(11) DEFAULT 0,
  `tarifMotor` int(11) DEFAULT NULL,
  `tarifMobil` int(11) DEFAULT NULL,
  `tarifTruk` int(11) DEFAULT NULL,
  PRIMARY KEY (`idParkiran`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `informasiparkiran`
--

LOCK TABLES `informasiparkiran` WRITE;
/*!40000 ALTER TABLE `informasiparkiran` DISABLE KEYS */;
/*!40000 ALTER TABLE `informasiparkiran` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kendaraan`
--

DROP TABLE IF EXISTS `kendaraan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kendaraan` (
  `idKendaraan` int(11) NOT NULL AUTO_INCREMENT,
  `platNomor` varchar(255) DEFAULT NULL,
  `jenis` varchar(255) DEFAULT NULL,
  `sedangParkir` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idKendaraan`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kendaraan`
--

LOCK TABLES `kendaraan` WRITE;
/*!40000 ALTER TABLE `kendaraan` DISABLE KEYS */;
/*!40000 ALTER TABLE `kendaraan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kendaraanterparkir`
--

DROP TABLE IF EXISTS `kendaraanterparkir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kendaraanterparkir` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idParkiran` int(11) NOT NULL,
  `idKendaraan` int(11) NOT NULL,
  `waktuMasuk` timestamp NULL DEFAULT NULL,
  `waktuKeluar` timestamp NULL DEFAULT NULL,
  `biaya` int(11) DEFAULT NULL,
  `sudahKeluar` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  CONSTRAINT `kendaraanterparkir_ibfk_1` FOREIGN KEY (`idParkiran`) REFERENCES `informasiparkiran` (`idParkiran`),
  CONSTRAINT `kendaraanterparkir_ibfk_2` FOREIGN KEY (`idKendaraan`) REFERENCES `kendaraan` (`idKendaraan`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kendaraanterparkir`
--

LOCK TABLES `kendaraanterparkir` WRITE;
/*!40000 ALTER TABLE `kendaraanterparkir` DISABLE KEYS */;
/*!40000 ALTER TABLE `kendaraanterparkir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Current Database: `parkco`
--

USE `parkco`;

--
-- Final view structure for view `account`
--

/*!50001 DROP TABLE IF EXISTS `account`*/;
/*!50001 DROP VIEW IF EXISTS `account`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `account` AS select `admin`.`email` AS `email`,`admin`.`username` AS `username`,`admin`.`password` AS `password` from `admin` union select `customer`.`email` AS `email`,`customer`.`username` AS `username`,`customer`.`password` AS `password` from `customer` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-13 13:48:13
