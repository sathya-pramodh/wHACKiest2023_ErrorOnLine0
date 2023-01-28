import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';

export default function NavigationBar() {
    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static">
                <Toolbar >
                    <Button type="submit" href='/home' sx={{ flexGrow: 1 }} color="inherit">Home</Button>
                    <Button type="submit" href="/login" sx={{ flexGrow: 1 }} color="inherit">Login</Button>
                </Toolbar>
            </AppBar>
        </Box >
    );
}
