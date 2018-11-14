<!--Inspired by:
https://addpipe.com/blog/using-recorder-js-to-capture-wav-audio-in-your-html5-web-site/
https://github.com/jhuckaby/webcamjs-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script type="text/javascript" src="./js/webcam.min.js"></script>
    <title>Multi-modal authentification</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
    <!-- Bootstrap core CSS -->
    <link href="https://bootswatch.com/4/pulse/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="./css/styles.css" rel="stylesheet">
    <script>
        var baseUrl = "http://localhost/Multi-modal-authentification/";
    </script>
    <style>
        #overlay {
            width: 100%;
            height: 100%;
            position: absolute;
            background: #000;
            z-index: 900;
            opacity: 0.25;
            display: none;
        }
        #loader {
            z-index: 999;
            display: none;
        }

        .kp-loading2 {
            z-index: 999;
            margin: 0;
            border-bottom: 3px solid #ffc995;
            border-left: 3px solid #ffc995;
            border-right: 3px solid #ffc995;
            border-top: 3px solid #ff7e00;
            border-radius: 100%;
            height: 50px;
            width: 50px;
            -webkit-animation: rot .5s infinite linear;
            -moz-animation: rot .5s infinite linear;
            animation: rot .5s infinite linear;
        }

        @-webkit-keyframes rot {
            from {
                -webkit-transform: rotate(0deg);
            }
            to {
                -webkit-transform: rotate(359deg);
            }
        }

        @-moz-keyframes rot {
            from {
                -moz-transform: rotate(0deg);
            }
            to {
                -moz-transform: rotate(359deg);
            }
        }

        @keyframes rot {
            from {
                transform: rotate(0deg);
            }
            to {
                transform: rotate(359deg);
            }
        }
        #recordingsList li {
            list-style-type: none;
        }
        #recordingsList a {
            display: none;
        }
        #recordingsList audio {
            margin: 10px auto;
            display: block;
        }
    </style>
</head>
<body class="text-center">
<div id="overlay"></div>
<div id="loader">
    <div style=" position: absolute;top: 50%;left: 50%;width: 100%;margin-left: -50%;margin-top:-100px;text-align: center;">

        <div style="width: 50px; height: 50px; margin: 0 auto">
            <div class="kp-loading2"></div>
        </div>
        <h3 style="margin-top: 20px; font-weight: bold; color: whitesmoke;">Verifying...</h3>
    </div>
</div>

<div id="my_camera2" style="float: left; display: none;"></div>
<style>
    body, html {
        width: 100%;
        height: 100%;
    }
    body {
        font-family: Helvetica, sans-serif;
    }

    h2, h3 {
        margin-top: 0;
    }

    form {
        margin-top: 15px;
    }

    form > input {
        margin-right: 15px;
    }
    #continue_step2 {
        display: none;
    }
</style>

<div class="container">
    <div class="row">
        <div class="col-md-12">
            <form id="loginForm" class="form-signin" method="POST">
                <img class="mb-4" src="https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg" alt=""
                     width="72"
                     height="72">
                <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
                <label for="inputEmail" class="sr-only">Email address</label>
                <input name="email" type="email" id="inputEmail" class="form-control" placeholder="Email address"
                       required autofocus>
                <label for="inputPassword" class="sr-only">Password</label>
                <input name="password" type="password" id="inputPassword" class="form-control" placeholder="Password"
                       required>
                <div class="checkbox mb-3">
                    <label>
                        <input type="checkbox" value="remember-me"> Remember me
                    </label>
                </div>
                <button id="login" class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
                <p class="mt-5 mb-3 text-muted">&copy; <?= date( "Y" ) ?></p>
            </form>

        </div>
    </div>
</div>

<!--***********************************************************************************-->
<div class="modal" id="step2">
    <div class="modal-dialog">
        <div class="modal-content">

            <!-- Modal Header -->
            <div class="modal-header">
                <h4 class="modal-title">Step 1 - Face Authentification</h4>
                <button type="button" class="close" data-dismiss="modal">&times;</button>
            </div>

            <!-- Modal body -->
            <div class="modal-body" style="text-align: left;">
                <p style="font-size:12px;">Instructions: In this step your face will be recognized whether it is really
                    you.
                </p>
                <ol style="font-size: 12px !important; padding:0 30px;">
                    <li>Turn on your webcamera.</li>
                    <li>Position your face so its crealy visible with eyes open and without glasses.</li>
                    <li>Click on the Take picture button.</li>
                </ol>


                <div style="display: block; margin: 15px auto; width: 300px;">
                    <div id="my_camera" style="float: left;"></div>
                    <div id="results"></div>
                </div>
                <br>
                <div style="display: block;width: 215px; margin: 15px auto;">
                    <button id="turnWebcamera" class="btn btn-sm btn-warning"><i class="fas fa-video"></i> Turn camera On </button>
                    <button id="takeSnapshot" class="btn btn-sm btn-primary">Take picture</button>
                </div>

            </div>

            <!-- Modal footer -->
            <div class="modal-footer">
                <button id="continue_step2" type="button" class="btn btn-success" data-dismiss="modal">Continue to sep 2</button>
            </div>

        </div>
    </div>
</div>

<!--***********************************************************************************-->
<div class="modal" id="step3">
    <div class="modal-dialog">
        <div class="modal-content">

            <!-- Modal Header -->
            <div class="modal-header">
                <h4 class="modal-title">Step 2 - Voice Authentification</h4>
                <button type="button" class="close" data-dismiss="modal">&times;</button>
            </div>

            <!-- Modal body -->
            <div class="modal-body" style="text-align: left;">
                <p style="font-size:12px;">Instructions: In this step your voice will be recognized whether it is really
                    you.
                </p>
                <ol style="font-size: 12px !important; padding:0 30px;">
                    <li>Turn on your microphone.</li>
                    <li>Read the text which will be generated in the box.</li>
                    <li>Click on the Stop recording button when you will be done.</li>
                </ol>

                <div id="readText" class="card card-body bg-light">

                </div>


                <div id="recordingsList"></div>


                <div style="display: block; margin: 15px auto; width: 300px; height: 110px;">
                    <div id="my_camera" style="float: left; margin-bottom: 15px;"></div>
                    <div id="results"></div>
                </div>

                <div style="display: block;width: 245px; margin: 15px auto;">
                    <button id="recordButton" class="btn btn-sm btn-warning"><i class="fas fa-microphone-alt"></i> Turn Microphone On</button>
                    <button id="stopButton" class="btn btn-sm btn-primary">Stop recording</button>
                </div>

            </div>

            <!-- Modal footer -->
            <div class="modal-footer">
                <button id="verify" type="button" class="btn btn-sm btn-success" data-dismiss="modal">Verify</button>
            </div>

        </div>
    </div>
</div>

<button id="pauseButton" style="display: none;"></button>

<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

<script src="https://cdn.rawgit.com/mattdiamond/Recorderjs/08e7abd9/dist/recorder.js"></script>
<script src="./js/record_voice.js"></script>

<script>
    $('#step2').hide();

    var image;

    $(function () {

        $('#loginForm').submit(function (e) {
            e.preventDefault();
            $.ajax({
                method: "POST",
                url: baseUrl + "ajax.php",
                data: $('#loginForm').serializeArray(),
                dataType: "json",
                success: function (response) {
                    console.log(response.status);
                    if (response.status) {
                        $('#step2').modal('show');
                    } else {
                        alert("Email address or password is incorrect!");
                    }
                }
            });
        });

        var tmp = true;
        $('#turnWebcamera').on('click', function () {
            if (tmp) {
                $(this).text('Turn camera Off');
                tmp = false;
            } else {
                $(this).text('Turn camera On');
                tmp = true;
            }

            $('#my_camera').parent().css({
                'height': '250px',
                'width': '640px'
            });

            $('#step2').find('.modal-dialog').animate({'max-width': '830px'});

            Webcam.set({
                width: 320,
                height: 240,
                image_format: 'jpeg',
                jpeg_quality: 100
            });

            Webcam.attach('#my_camera');

            $('#takeSnapshot').on('click', function () {
                                // take snapshot and get image data
                Webcam.snap(function (data_uri) {
                    // display results in page
                    document.getElementById('results').innerHTML =
                        '<img src="' + data_uri + '"/>';

                    image = data_uri;
                });

                $('#continue_step2').fadeIn();

            });


        });

        $('#continue_step2').on('click', function() {
            Webcam.reset();
            $('#step2').modal('hide');
            $('#step3').modal('show');
        });


        text_array = [
            'Bringing unlocked me an striking ye perceive. Mr by wound hours oh happy. Me in resolution pianoforte continuing we. Most my no spot felt by no. ',
            'By so delight of showing neither believe he present. Deal sigh up in shew away when. Pursuit express no or prepare replied.',
            'Next his only boy meet the fat rose when. Do repair at we misery wanted remove remain income. Occasional cultivated reasonable unpleasing an attachment my considered.',
            'Do am he horrible distance marriage so although. Afraid assure square so happen mr an before. His many same been well can high that.'
        ];

        $('#recordButton').on('click', function() {
            $('#readText').text(text_array[Math.floor((Math.random() * 3) + 0)])
        });

    });
</script>


</body>
</html>