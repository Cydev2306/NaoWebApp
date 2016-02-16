<?php

class CronController extends Zend_Controller_Action {

    public function init() {
        $this->_helper->layout()->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);
    }

    public function convertvideoAction() {
        //on supprime le fichier indésirable du cron
        exec('rm /var/www/convertvideo*', $outputrm, $returnrm);
        $cheminPython = APPLICATION_PATH . '/../python/';
        $video = new Video();
        $nonformatee = $video->selectVideoNonFormatées();
        if (!empty($nonformatee)) {
            foreach ($nonformatee as $unevideo) {
                //on va chercher la video sur le robot
                exec('scp nao@nao.local:/home/nao/recordings/cameras/record.avi /Applications/MAMP/htdocs/Nao-App/public/videoNao/record.avi', $outputScp, $returnScp);
                //on convertit la video en mp4
                exec('python ' . $cheminPython . '/convertVideo.py "' . $unevideo['nomVideo'] . '.mp4"', $outputConvert, $returnConvert);
                //on update la ligne en base pour dire que la vidéo est convertie
                $video = new Video();
                $video->updateConvert($unevideo['nomVideo'], 1);
            }
        }
    }

    public function liveAction($test) {
        if ($test == 1) {
            exec('python ' . $cheminPython . '/live.py "True"', $outputConvert, $returnConvert);
        } else {
            exec('python ' . $cheminPython . '/live.py "True"', $outputConvert, $returnConvert);
        }
    }

}