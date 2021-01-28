-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: Lifechoicesonline
-- ------------------------------------------------------
-- Server version	8.0.22-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `surname` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `department` varchar(60) DEFAULT NULL,
  `signin` datetime NOT NULL,
  `signout` datetime DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES (1,'siphenkosi','salman','salmansiphenkosi@gmail.com','Academy','2021-01-24 18:29:38','2021-01-24 19:04:24'),(2,'azipheli','mahela','nwmahela@gmail.com','Finance','2021-01-24 18:41:42','2021-01-26 14:53:54'),(3,'nkuthazo','mkunyana','nkura@gmail.com','Studio','2021-01-24 18:42:42','2021-01-25 16:29:30'),(4,'siphenkosi','salman','salmansiphenkosi@gmail.com','Academy','2021-01-24 18:55:39','2021-01-24 19:04:24'),(5,'siphenkosi','salman','salmansiphenkosi@gmail.com','Academy','2021-01-24 18:57:49','2021-01-24 19:04:24'),(6,'yamkela','salman','yamkela@gmail.com','Academy','2021-01-25 17:17:53','2021-01-26 14:06:05'),(7,'yamkela','salman','yamkela@gmail.com','Academy','2021-01-25 18:19:59','2021-01-26 14:06:05'),(8,'yamkela','salman','yamkela@gmail.com','Academy','2021-01-26 13:31:02','2021-01-26 14:06:05'),(9,'yamkela','salman','yamkela@gmail.com','Academy','2021-01-26 14:13:38','2021-01-26 14:45:13'),(10,'yamkela','salman','yamkela@gmail.com','Academy','2021-01-26 14:47:11','2021-01-26 14:51:00'),(11,'siphenkosi','salman','salmansiphenkosi@gmail.com','Academy','2021-01-26 14:47:53','2021-01-26 14:51:56'),(12,'test','sub','test@gmail.com','Studio','2021-01-28 06:04:36','2021-01-28 06:15:25');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `surname` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(60) NOT NULL,
  `role` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (6,'siphenkosi','salman','salmansiphenkosi@gmail.com','salman2021','Admin'),(7,'test','testing','test@testing.co.za','test2021','User');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-28 19:46:20
