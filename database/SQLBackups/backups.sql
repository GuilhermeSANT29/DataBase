BACKUP DATABASE [TEST_DB] 
TO DISK = N'C:\SQLBackups\test_db.bak' 
WITH FORMAT, 
     INIT, 
     NAME = 'Backup Completo de TEST_DB', 
     MEDIANAME = 'SQLServerBackup';