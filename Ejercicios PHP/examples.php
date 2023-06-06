<?php
    declare(strict_types=1);
    const COLORS = [["uno", 2, "tres"],["cuatro", 5, "seis"], ["siete", 8, "nueve"]];
    function colorCode(string $color)
    {
        $tolower = strtolower($color);
        $colors_array = array(
            'black' => 0,
            'brown' => 1,
            'red' => 2,
            'orange' => 3,
            'yellow' => 4,
            'green' => 5,
            'blue' => 6,
            'violet' => 7,
            'grey' => 8,
            'white' => 9,
            'colors' => ["black","brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
        );
        return $colors_array[$tolower];
                
    }
foreach (COLORS as $keyF => $fila) {
    foreach($fila as $keyC => $valor){
        print_r("Fila ". $keyF . "Columna ". $keyC . $valor . " ");
    }
}