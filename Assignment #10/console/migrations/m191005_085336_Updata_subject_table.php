<?php

use yii\db\Migration;

/**
 * Class m191005_085336_Updata_subject_table
 */
class m191005_085336_Updata_subject_table extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->addColumn('subject','created_at',$this->integer());
        $this->addColumn('subject','created_by',$this->integer());
        $this->addColumn('subject','updated_at',$this->integer());
        $this->addColumn('subject','updated_by',$this->integer());
    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        echo "m191005_085336_Updata_subject_table cannot be reverted.\n";

        return false;
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m191005_085336_Updata_subject_table cannot be reverted.\n";

        return false;
    }
    */
}
