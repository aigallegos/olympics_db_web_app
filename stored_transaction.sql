DELIMITER $$
CREATE DEFINER=`root`@`%` PROCEDURE `my_transaction`(country_code1 VARCHAR(255), discipline_name1 VARCHAR(255))
BEGIN
  DECLARE i INT DEFAULT 0;
  DROP TABLE IF EXISTS result_table;
  CREATE TEMPORARY TABLE result_table (name VARCHAR(255), country VARCHAR(255), discipline VARCHAR(255));
  
  SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
  START TRANSACTION;
  
  WHILE i < 2 DO
    IF i = 0 THEN
      INSERT INTO result_table
      SELECT Athlete.name, Athlete.CCA3, Athlete.discipline_name FROM Athlete WHERE Athlete.CCA3 = country_code1 AND Athlete.discipline_name = discipline_name1
      UNION
      SELECT Coach.name, Coach.CCA3, Coach.discipline_name FROM Coach WHERE Coach.CCA3 = country_code1 AND Coach.discipline_name = discipline_name1;
	ELSE
	  INSERT INTO result_table
      SELECT Athlete.name, Athlete.CCA3, Athlete.discipline_name FROM Athlete WHERE Athlete.CCA3 = country_code1 AND Athlete.discipline_name != discipline_name1
      UNION
      SELECT Coach.name, Coach.CCA3, Coach.discipline_name FROM Coach WHERE Coach.CCA3 = country_code1 AND Coach.discipline_name != discipline_name1;
    END IF;
    
    SET i = i + 1;
  END WHILE;
  
  COMMIT;

  SELECT * FROM result_table;
END$$
DELIMITER ;