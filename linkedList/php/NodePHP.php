<?php

class NodePHP {
    public int $data;
    public ?NodePHP $next;

    public function __construct(int $data) {
        $this->data = $data;
        $this->next = null;
    }
}