<?php
/*
 * Pretend that this look into database and everything is safe
 *
*/


/*
 * Verify email and password.
 */
if ( ! empty( $_POST ) && isset( $_POST['email'] ) && isset( $_POST['password'] ) ) {
    if ( $_POST['email'] === 'lstran17@student.aau.dk' && $_POST['password'] === 'vgis9' ) {
        echo json_encode( [
            'status' => TRUE
        ] );
    } else {
        echo json_encode( [
            'status' => FALSE
        ] );
    }
}

/*
 * Process the image
 */
if (! empty( $_POST ) && isset($_POST['image'])) {
    
}
