<?

addrList();

function addrList() {
	try {
		$db = getConnection();
		echo "<table border='1'>";
		foreach($db->query("SELECT * FROM addressbook") as $row) {
			echo "<tr>";
			echo "<td>";
			echo $row['name']; 
			echo "</td>";

			echo "<td>";
			echo $row['phone']; 
			echo "</td>";

			echo "<td>";
			echo "<a href='http://" . $row['website'] . "'>";
			echo $row['website']; 
			echo "</a>";
			echo "</td>";
			echo "</tr>";
		}
		echo "</table>";
	} catch(PDOException $e) {
		echo "DB error:" . $e->getMessage(); 
	}
}

function getConnection() {
	$dbhost="127.0.0.1";
	$dbuser="root";
	$dbpass="ariag25";
	$dbname="mydb";
	$dbh = new PDO("mysql:host=$dbhost;dbname=$dbname", $dbuser, $dbpass);	
	$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	return $dbh;
}
?>
