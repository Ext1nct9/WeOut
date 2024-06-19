import AppBar from '@mui/material/AppBar'
import Box from '@mui/material/Box'
import Toolbar from '@mui/material/Toolbar'
import Button from '@mui/material/Button'
import { Typography } from '@mui/material'

export default function TopBar() {
    /**
    const dispatch = useAppDispatch()
    const isLoggedIn = useAppSelector(selectIsLoggedIn)

    async function handleLogout() {
        try {
            let action = await dispatch(logout({}))
            if (action.error) {
                throw action.error
            }
            window.alert('Logout successful')
            window.location.href = '/'
        } catch (error) {
            window.alert(`${error.message}`)
            console.error(error)
        }
    }
        */


    return (
        <Box sx={{ flexGrow: 1 }} color ='transparent'>
            <AppBar position='static' color = 'transparent'>
                <Toolbar sx={{ justifyContent: 'space-between' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center' }}>
                        <Button color='primary' href='/'>
                            WeOut
                        </Button>
                        <Typography variant='h6' color= 'primary' component='div'>
                            in
                        </Typography>
                        <Button color='primary' href='/event'>
                            Montreal
                        </Button>
                    </Box>
                    <Box sx={{ display: 'flex', alignItems: 'center' }}>
                            <Button
                                color='primary'
                                sx={{ marginLeft: 5 }}
                                href='/login'
                            >
                                Sign in
                            </Button>
                            <Button color='primary' href='/search'>
                                Search All Events
                            </Button>
                    </Box>
                </Toolbar>
            </AppBar>
        </Box>

    )
}