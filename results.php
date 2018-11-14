<?php
$handle = fopen( "fused_probabilities.log", "r" );
if ( $handle ) {
    $logs = [];
    while ( ( $line = fgets( $handle ) ) !== FALSE ) {
        $tmp    = explode( '_', $line );
        $logs[] = [
            'datetime'   => $tmp[0],
            'facelabel'  => $tmp[2],
            'faceacc'    => $tmp[4],
            'voiceacc'   => $tmp[6],
            'voicelabel' => $tmp[8],
            'fusionacc' => $tmp[10],
        ];
    }
    $logs = array_reverse( $logs );
    fclose( $handle );
} else {
    // error opening the file.
}
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title></title>
    <link href="https://bootswatch.com/4/pulse/bootstrap.css" rel="stylesheet">
    <style>
        tbody tr:first-child {
            background: #F2F6FA;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <h1 style="text-align:center; margin: 20px 0;">Logs</h1>
            <table class="table">
                <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Datetime</th>
                    <th scope="col">Face label</th>
                    <th scope="col">Face probability</th>
                    <th scope="col">Voice label</th>
                    <th scope="col">Voice probability</th>
                    <th scope="col">Fusion of probabilities</th>
                </tr>
                </thead>
                <tbody>
                <?php $i = 1;
                foreach ( $logs as $log ): ?>
                    <tr>
                        <td><?= $i ?></td>
                        <td><?= $log['datetime'] ?></td>
                        <td><?= $log['facelabel'] ?></td>
                        <td><?= $log['faceacc'] ?></td>
                        <td><?= $log['voicelabel'] ?></td>
                        <td><?= $log['voiceacc'] ?></td>
                        <td><?= $log['fusionacc'] ?></td>
                    </tr>
                <?php $i++; endforeach; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>
</body>
</html>
