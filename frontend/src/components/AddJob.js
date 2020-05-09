import React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: 200,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
}));

function AddJob() {
  const classes = useStyles();

  const [state, setState] = React.useState({
    ins: '',
    name: 'hai',
  });

  const handleChange = (event) => {
    const name = event.target.name;
    setState({
      ...state,
      [name]: event.target.value,
    });
  };


  return (
    <div>
      <h2>Add Jobs here</h2>
      <Grid container spacing={1}>
        <Grid item xs>
          <FormControl variant="outlined" className={classes.formControl}>
            <InputLabel htmlFor="filled-ins-native-simple" fullWidth>Select Instance</InputLabel>
            <Select
              native
              value={state.ins}
              onChange={handleChange}
              inputProps={{
                name: 'ins',
                id: 'filled-ins-native-simple',
              }}
            >
              <option aria-label="None" value="" />
              <option value="PS1">PS_1</option>
              <option value="PS2">PS_2</option>
              <option value="PS3">PS_3</option>
            </Select>
          </FormControl>
        </Grid>

        <Grid item xs={12}>
          <TextField id="outlined-basic" label="Job Name" variant="outlined" fullWidth style={{margin: 10}} />
        </Grid>

        <Grid item xs={12}>
          <TextField id="outlined-basic" label="Script Path" variant="outlined" fullWidth style={{ margin: 10}} />
        </Grid>

        <Grid item xs={12}>
        <Button variant="contained" color="primary" style={{ margin: 'auto', display: 'block'  }}>
          Primary
        </Button>
        </Grid>

      </Grid>
    </div>
  )
}

export default AddJob;
