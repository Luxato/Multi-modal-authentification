<?php

// Writes voice and image int othe file
$image = substr($_POST['image'], 23);

$success = file_put_contents( 'image.jpg', base64_decode($image) );


$fp = fopen( 'data2.json', 'w' );
fwrite( $fp, json_encode( [
    'image' => 'image.jpg',
    'voice' => $_POST['voice_path']
] ) );
fclose( $fp );

echo json_encode( [
    'status' => TRUE
] );