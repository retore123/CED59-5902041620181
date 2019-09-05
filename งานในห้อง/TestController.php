<?php
namespace frontend\controllers;

use yii\web\Controllers;

class TestController extends Controller
{
    public function actionIndex()
    {
        
        $data = 'test';
        return $this->render('index', 
        [
            'xdata' => $data
            
        ]);
    }

    public function actionTest() 
    {
        echo 'test';
        return $this->render('test');
    }


}