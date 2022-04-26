Enter password: 
-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: cricket
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.21.04.3

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
-- Table structure for table `Batsman`
--

DROP TABLE IF EXISTS `Batsman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Batsman` (
  `Batsman_Type` varchar(255) DEFAULT NULL,
  `Player_id` int NOT NULL,
  PRIMARY KEY (`Player_id`),
  CONSTRAINT `Batsman_ibfk_1` FOREIGN KEY (`Player_id`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Batsman`
--

LOCK TABLES `Batsman` WRITE;
/*!40000 ALTER TABLE `Batsman` DISABLE KEYS */;
INSERT INTO `Batsman` VALUES ('Right',1),('Right',4),('Right',7),('Left',10);
/*!40000 ALTER TABLE `Batsman` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Batsman_Total_Runs`
--

DROP TABLE IF EXISTS `Batsman_Total_Runs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Batsman_Total_Runs` (
  `Runs_in_ODI` int DEFAULT NULL,
  `Runs_in_T20` int DEFAULT NULL,
  `Runs_in_Test` int DEFAULT NULL,
  `Player_id` int NOT NULL,
  PRIMARY KEY (`Player_id`),
  CONSTRAINT `Batsman_Total_Runs_ibfk_1` FOREIGN KEY (`Player_id`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Batsman_Total_Runs`
--

LOCK TABLES `Batsman_Total_Runs` WRITE;
/*!40000 ALTER TABLE `Batsman_Total_Runs` DISABLE KEYS */;
INSERT INTO `Batsman_Total_Runs` VALUES (301,201,100,1),(302,202,101,4),(303,203,102,7),(304,204,103,10);
/*!40000 ALTER TABLE `Batsman_Total_Runs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bowler`
--

DROP TABLE IF EXISTS `Bowler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bowler` (
  `Bowling_type` varchar(255) DEFAULT NULL,
  `Average_bowling_speed` float DEFAULT NULL,
  `Economy` float DEFAULT NULL,
  `Player_id` int NOT NULL,
  PRIMARY KEY (`Player_id`),
  CONSTRAINT `Bowler_ibfk_1` FOREIGN KEY (`Player_id`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bowler`
--

LOCK TABLES `Bowler` WRITE;
/*!40000 ALTER TABLE `Bowler` DISABLE KEYS */;
INSERT INTO `Bowler` VALUES ('Spin',100,8.01,2),('Spin',100,8.06,5),('spin',100,5.01,6),('Fast',140,10.45,8),('Fast',150,10.58,11);
/*!40000 ALTER TABLE `Bowler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Coach_Phone_NO`
--

DROP TABLE IF EXISTS `Coach_Phone_NO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Coach_Phone_NO` (
  `Coach_ID` int NOT NULL,
  `Phone_Numbers` int NOT NULL,
  PRIMARY KEY (`Coach_ID`,`Phone_Numbers`),
  CONSTRAINT `Coach_Phone_NO_ibfk_1` FOREIGN KEY (`Coach_ID`) REFERENCES `coach` (`Coach_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Coach_Phone_NO`
--

LOCK TABLES `Coach_Phone_NO` WRITE;
/*!40000 ALTER TABLE `Coach_Phone_NO` DISABLE KEYS */;
INSERT INTO `Coach_Phone_NO` VALUES (1,123456),(2,234567),(3,345678),(4,456789);
/*!40000 ALTER TABLE `Coach_Phone_NO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Coached_by`
--

DROP TABLE IF EXISTS `Coached_by`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Coached_by` (
  `Coach_id` int NOT NULL,
  `Player_id` int NOT NULL,
  KEY `Coach_id` (`Coach_id`),
  KEY `Player_id` (`Player_id`),
  CONSTRAINT `Coached_by_ibfk_1` FOREIGN KEY (`Coach_id`) REFERENCES `coach` (`Coach_ID`),
  CONSTRAINT `Coached_by_ibfk_2` FOREIGN KEY (`Player_id`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Coached_by`
--

LOCK TABLES `Coached_by` WRITE;
/*!40000 ALTER TABLE `Coached_by` DISABLE KEYS */;
INSERT INTO `Coached_by` VALUES (1,1),(1,2),(1,3),(2,4),(2,5),(2,6),(3,7),(3,8),(3,9),(4,10),(4,11),(4,12);
/*!40000 ALTER TABLE `Coached_by` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Earns`
--

DROP TABLE IF EXISTS `Earns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Earns` (
  `Manager_id` int NOT NULL,
  `Coach_id` int NOT NULL,
  `Player_id` int NOT NULL,
  PRIMARY KEY (`Manager_id`,`Coach_id`,`Player_id`),
  KEY `Coach_id` (`Coach_id`),
  KEY `Player_id` (`Player_id`),
  CONSTRAINT `Earns_ibfk_1` FOREIGN KEY (`Manager_id`) REFERENCES `Manager` (`Manager_ID`),
  CONSTRAINT `Earns_ibfk_2` FOREIGN KEY (`Coach_id`) REFERENCES `coach` (`Coach_ID`),
  CONSTRAINT `Earns_ibfk_3` FOREIGN KEY (`Player_id`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Earns`
--

LOCK TABLES `Earns` WRITE;
/*!40000 ALTER TABLE `Earns` DISABLE KEYS */;
/*!40000 ALTER TABLE `Earns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manager`
--

DROP TABLE IF EXISTS `Manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Manager` (
  `Manager_ID` int NOT NULL,
  `Manager_First_Name` varchar(255) DEFAULT NULL,
  `Manager_Middle_Name` varchar(255) DEFAULT NULL,
  `Manager_Last_Name` varchar(255) DEFAULT NULL,
  `Club_ID` int NOT NULL,
  `Team_ID` int NOT NULL,
  PRIMARY KEY (`Manager_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manager`
--

LOCK TABLES `Manager` WRITE;
/*!40000 ALTER TABLE `Manager` DISABLE KEYS */;
INSERT INTO `Manager` VALUES (1,'Hardik','Oyo','Gupta',1,1),(2,'Shreyash','Boss','Jain',1,2),(3,'Venika','GodKnows','Sruthi',2,3),(4,'Thanos','Power','Hulk',2,4);
/*!40000 ALTER TABLE `Manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manager_Phone_No`
--

DROP TABLE IF EXISTS `Manager_Phone_No`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Manager_Phone_No` (
  `Manager_ID` int NOT NULL,
  `Phone_Number` varchar(255) NOT NULL,
  PRIMARY KEY (`Manager_ID`,`Phone_Number`),
  CONSTRAINT `Manager_Phone_No_ibfk_1` FOREIGN KEY (`Manager_ID`) REFERENCES `Manager` (`Manager_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manager_Phone_No`
--

LOCK TABLES `Manager_Phone_No` WRITE;
/*!40000 ALTER TABLE `Manager_Phone_No` DISABLE KEYS */;
INSERT INTO `Manager_Phone_No` VALUES (1,'11111'),(2,'22222'),(2,'55555'),(3,'33333'),(4,'44444');
/*!40000 ALTER TABLE `Manager_Phone_No` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Matches_played`
--

DROP TABLE IF EXISTS `Matches_played`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Matches_played` (
  `Player_id` int NOT NULL,
  `Test_match` int DEFAULT NULL,
  `One_day` int DEFAULT NULL,
  `T20` int DEFAULT NULL,
  PRIMARY KEY (`Player_id`),
  CONSTRAINT `Matches_played_ibfk_1` FOREIGN KEY (`Player_id`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Matches_played`
--

LOCK TABLES `Matches_played` WRITE;
/*!40000 ALTER TABLE `Matches_played` DISABLE KEYS */;
INSERT INTO `Matches_played` VALUES (1,11,15,20),(2,10,10,10),(3,11,15,20),(4,100,100,100),(5,15,18,30),(6,15,18,30),(7,18,21,40),(8,18,21,40),(9,19,21,40),(10,17,30,50),(11,16,30,50),(12,17,30,50);
/*!40000 ALTER TABLE `Matches_played` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Team`
--

DROP TABLE IF EXISTS `Team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Team` (
  `Team_ID` int NOT NULL,
  `Team_Name` varchar(255) DEFAULT NULL,
  `Club_ID` int NOT NULL,
  `Managed_by_ID` int NOT NULL,
  `Numbers_of_Players` int DEFAULT NULL,
  PRIMARY KEY (`Team_ID`),
  KEY `Managed_by_ID` (`Managed_by_ID`),
  CONSTRAINT `Team_ibfk_1` FOREIGN KEY (`Managed_by_ID`) REFERENCES `Manager` (`Manager_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Team`
--

LOCK TABLES `Team` WRITE;
/*!40000 ALTER TABLE `Team` DISABLE KEYS */;
INSERT INTO `Team` VALUES (1,'Under-19',1,1,3),(2,'Under-17',1,2,3),(3,'Under-18',2,3,3),(4,'Under-21',2,4,3);
/*!40000 ALTER TABLE `Team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Wicket_keeper`
--

DROP TABLE IF EXISTS `Wicket_keeper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Wicket_keeper` (
  `Number_of_stumpings` int DEFAULT NULL,
  `Player_id` int NOT NULL,
  PRIMARY KEY (`Player_id`),
  CONSTRAINT `Wicket_keeper_ibfk_1` FOREIGN KEY (`Player_id`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Wicket_keeper`
--

LOCK TABLES `Wicket_keeper` WRITE;
/*!40000 ALTER TABLE `Wicket_keeper` DISABLE KEYS */;
INSERT INTO `Wicket_keeper` VALUES (10,3),(11,6),(11,9),(12,12);
/*!40000 ALTER TABLE `Wicket_keeper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `club`
--

DROP TABLE IF EXISTS `club`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `club` (
  `Club_ID` int NOT NULL,
  `Club_Name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Club_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `club`
--

LOCK TABLES `club` WRITE;
/*!40000 ALTER TABLE `club` DISABLE KEYS */;
INSERT INTO `club` VALUES (1,'India'),(2,'AlsoIndia'),(3,'NotIndia');
/*!40000 ALTER TABLE `club` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coach`
--

DROP TABLE IF EXISTS `coach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coach` (
  `Coach_ID` int NOT NULL,
  `Club_ID` int NOT NULL,
  `Coach_Name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Coach_ID`),
  KEY `Club_ID` (`Club_ID`),
  CONSTRAINT `coach_ibfk_1` FOREIGN KEY (`Club_ID`) REFERENCES `club` (`Club_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coach`
--

LOCK TABLES `coach` WRITE;
/*!40000 ALTER TABLE `coach` DISABLE KEYS */;
INSERT INTO `coach` VALUES (1,1,'Kapil Dev'),(2,1,'Anil Kumble'),(3,2,'Ravi Shastri'),(4,2,'Gadhe ka Baccha');
/*!40000 ALTER TABLE `coach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coach_type`
--

DROP TABLE IF EXISTS `coach_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coach_type` (
  `Coach_id` int NOT NULL,
  `Type_name` varchar(255) NOT NULL,
  PRIMARY KEY (`Coach_id`,`Type_name`),
  CONSTRAINT `coach_type_ibfk_1` FOREIGN KEY (`Coach_id`) REFERENCES `coach` (`Coach_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coach_type`
--

LOCK TABLES `coach_type` WRITE;
/*!40000 ALTER TABLE `coach_type` DISABLE KEYS */;
INSERT INTO `coach_type` VALUES (1,'Useless'),(2,'Useless'),(3,'More useless'),(4,'like venika');
/*!40000 ALTER TABLE `coach_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `Player_ID` int NOT NULL,
  `Team_ID` int DEFAULT NULL,
  `Club_ID` int NOT NULL,
  `Player_First_Name` varchar(255) DEFAULT NULL,
  `Player_Middle_Name` varchar(255) DEFAULT NULL,
  `Player_Last_Name` varchar(255) DEFAULT NULL,
  `Number_of_matches_played` int DEFAULT NULL,
  PRIMARY KEY (`Player_ID`),
  KEY `Club_ID` (`Club_ID`),
  CONSTRAINT `player_ibfk_1` FOREIGN KEY (`Club_ID`) REFERENCES `club` (`Club_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES (1,1,1,'Justin','Selena','Bieber',100),(2,1,1,'Shawn','Camila','Mendes',30),(3,1,1,'Virat','Anushka','Kohli',37),(4,2,1,'Harry','Taylor','Style',56),(5,2,1,'Ranveer','Deepika','singh',57),(6,2,1,'Alia','Ranbeer','Bhatt',58),(7,3,2,'Nick','Priyanka','Jonas',67),(8,3,2,'Mahendra','Singh','Dhoni',68),(9,3,2,'kuch','bhi','maanlo',69),(10,4,2,'Yujvendra','Dhanshree','Chahal',69),(11,4,2,'Rahul','YouKnowWho','Chahar',69),(12,4,2,'koi','project','kardo',70);
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_Coaches_id`
--

DROP TABLE IF EXISTS `player_Coaches_id`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_Coaches_id` (
  `Player_ID` int NOT NULL,
  `Coach_id` int NOT NULL,
  PRIMARY KEY (`Player_ID`,`Coach_id`),
  KEY `Coach_id` (`Coach_id`),
  CONSTRAINT `player_Coaches_id_ibfk_1` FOREIGN KEY (`Coach_id`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_Coaches_id`
--

LOCK TABLES `player_Coaches_id` WRITE;
/*!40000 ALTER TABLE `player_Coaches_id` DISABLE KEYS */;
INSERT INTO `player_Coaches_id` VALUES (1,1),(2,1),(3,1),(4,2),(5,2),(6,2),(7,3),(8,3),(9,3),(10,4),(11,4),(12,4);
/*!40000 ALTER TABLE `player_Coaches_id` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_Phone_NO`
--

DROP TABLE IF EXISTS `player_Phone_NO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_Phone_NO` (
  `Player_ID` int NOT NULL,
  `Phone_Number` varchar(255) NOT NULL,
  PRIMARY KEY (`Player_ID`,`Phone_Number`),
  CONSTRAINT `player_Phone_NO_ibfk_1` FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_Phone_NO`
--

LOCK TABLES `player_Phone_NO` WRITE;
/*!40000 ALTER TABLE `player_Phone_NO` DISABLE KEYS */;
INSERT INTO `player_Phone_NO` VALUES (1,'248813'),(1,'313148'),(2,'253373'),(3,'585134'),(4,'349274'),(5,'258264'),(5,'695225'),(6,'989822'),(7,'549527'),(7,'644651'),(8,'822552'),(9,'342914'),(10,'594431'),(11,'967713'),(12,'166157');
/*!40000 ALTER TABLE `player_Phone_NO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_age`
--

DROP TABLE IF EXISTS `player_age`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_age` (
  `Date_of_Birth` int DEFAULT NULL,
  `Player_ID` int NOT NULL,
  PRIMARY KEY (`Player_ID`),
  CONSTRAINT `player_age_ibfk_1` FOREIGN KEY (`Player_ID`) REFERENCES `player` (`Player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_age`
--

LOCK TABLES `player_age` WRITE;
/*!40000 ALTER TABLE `player_age` DISABLE KEYS */;
INSERT INTO `player_age` VALUES (11012002,1),(12012002,2),(14022002,3),(11012004,4),(12012004,5),(12012004,6),(11012003,7),(12012003,8),(14022003,9),(11012000,10),(12012000,11),(14022000,12);
/*!40000 ALTER TABLE `player_age` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-26 11:50:34
