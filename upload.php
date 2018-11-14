<?php

/*Upload recording to server*/

$input = $_FILES['audio_data']['tmp_name'];

/*echo '<pre>';
print_r( $input );
echo '</pre>';*/
/*var_dump(file_exists($input));*/
/*echo '<pre>';
print_r( __DIR__ . '\\' . $output );
echo '</pre>';*/

move_uploaded_file( $input, './uploads/audio_recording.wav' );


echo json_encode( [
    'path' => './uploads/audio_recording.wav'
] );