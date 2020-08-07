<!DOCTYPE html>
<html>
    <head>
        <title>Postgre interface</title>
        <link rel="stylesheet" type="text/css" href="style.css">
        <meta charset="utf-8">
        <link rel="shortcut icon" href="#" />
    </head>

    <body>
        <?php
            include 'conf-db.php';

            $input_selishte_name = $_POST['selishte'];
            $input_selishte_type = $_POST['type'];
            $input_obstina_name = $_POST['obstina'];
            $input_oblast_name = $_POST['oblast'];

            if($input_selishte_name != "" || $input_selishte_type != "" || $input_obstina_name != "" || $input_oblast_name != "" )
            {
                $dbConnection = new PDO('pgsql:host='. $dbhost_ . ';dbname=' . $dbname_, $dbuser_, $dbpass_) or die("Connection failed");
            
                $dbConnection->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
                $dbConnection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
                $sql_query = 'select s.id, s.name as selishte_name, s.type as selishte_type, s.obstina_id, 
                                obst.name as obstina_name, obst.oblast_id, 
                                obl.name as oblast_name from public."selishta" as s 
                                inner join public."obstini" as obst on s.obstina_id=obst.id inner join public."oblasti" as obl on obst.oblast_id=obl.id  
                                where';
    
                $params = array();
    
                if($input_selishte_name != "")
                {
                    $sql_query = $sql_query . " s.name = :input_selishte_name";
                    $params["input_selishte_name"] = $input_selishte_name;
                }

                if($input_selishte_type != "")
                {
                    if($input_selishte_name != "")
                    {
                        $sql_query = $sql_query . " and s.type = :input_selishte_type";
                    }
                    else
                    {
                        $sql_query = $sql_query . " s.type = :input_selishte_type";
                    }

                    $params["input_selishte_type"] = $input_selishte_type;
                }

                if($input_obstina_name != "")
                {
                    if($input_selishte_name != "" || $input_selishte_type != "")
                    {
                        $sql_query = $sql_query . " and obst.name = :input_obstina_name";
                    }
                    else
                    {
                        $sql_query = $sql_query . " obst.name = :input_obstina_name";
                    }
                    
                    $params["input_obstina_name"] = $input_obstina_name;
                }
                
                if($input_oblast_name != "")
                {
                    if($input_selishte_name != "" || $input_selishte_type != "" || $input_obstina_name != "")
                    {
                        $sql_query = $sql_query . " and obl.name = :input_oblast_name";
                    }
                    else
                    {
                        $sql_query = $sql_query . " obl.name = :input_oblast_name";
                    }

                    $params["input_oblast_name"] = $input_oblast_name;
                }
                
                $statement = $dbConnection->prepare($sql_query);
                $statement->execute($params);
                $result = $statement->fetchAll();
    
                if(count($result) <= 0)
                {
                    echo "<p>The input data is not matching any records</p><br>";
                }
            }
        ?>

        <form name="Form" class="margin_style" action="" method="post" accept-charset="UTF-8">
            <div class="autocomplete" style="width:300px">
                <label for="city">Име на селище</label><br>
                <input type="text" id="selishte" name="selishte"
                            value="<?php if (isset($_POST["selishte"])) echo $_POST["selishte"]; ?>"><br><br>
            </div>

            <div class="autocomplete" style="width:300px">
                <label for="city">Тип на селището (гр./с.)</label><br>
                <input type="text" id="type" name="type"
                            value="<?php if (isset($_POST["type"])) echo $_POST["type"]; ?>"><br><br>
                    <select id="type" name="type">
                        <option value="">-</option>
                        <option value="гр.">Град</option>
                        <option value="с.">Село</option>
                    </select>
            </div><br>

            <div class="autocomplete" style="width:300px">
                <label for="city">Име на община</label><br>
                <input type="text" id="obstina" name="obstina"
                            value="<?php if (isset($_POST["obstina"])) echo $_POST["obstina"]; ?>"><br><br>
            </div>

            <div class="autocomplete" style="width:300px">
                <label for="city">Име на област</label><br>
                <input type="text" id="oblast" name="oblast"
                            value="<?php if (isset($_POST["oblast"])) echo $_POST["oblast"]; ?>"><br><br>
            </div>

            <input class="button button_style" type="submit" value="Submit" name="Submit"> <br><br>
        </form>

        <p>
            Count of records in table "oblasti": 28
        </p>

        <p>
            Count of records in table "obstini": 265
        </p>

        <p>
            Count of records in table "obstini": 5257
        </p>

        <table id="customers">
            <thead>
                <tr>
                    <th>id</th>
                    <th>selishte_name</th>
                    <th>selisthe_type</th>
                    <th>obstina_id</th>
                    <th>obstina_name</th>
                    <th>oblast_id</th>
                    <th>oblast_name</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach($result as $row) : ?>
                    <tr>
                        <td><?php echo htmlspecialchars($row["id"]) ?></td>
                        <td><?php echo htmlspecialchars($row["selishte_name"]) ?></td>
                        <td><?php echo htmlspecialchars($row["selishte_type"]) ?></td>
                        <td><?php echo htmlspecialchars($row["obstina_id"]) ?></td>
                        <td><?php echo htmlspecialchars($row["obstina_name"]) ?></td>
                        <td><?php echo htmlspecialchars($row["oblast_id"]) ?></td>
                        <td><?php echo htmlspecialchars($row["oblast_name"]) ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </body>
</html>